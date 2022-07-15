from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from auth import AuthHandler
import uvicorn 
import pandas as pd
import config
import converter


# currency converter schema
class base_param(BaseModel):
      amount: float 
      from_currency : str
      to_currency : str

# authentication schema 
class AuthDetails(BaseModel):
    username: str
    password: str

app = FastAPI(debug=True)


auth_handler = AuthHandler()
users = []



# create new user
@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):

    # check for available usernames 
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    
    # hash and save new user password 
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password    
    })
    return 'registered'


# user login
@app.post('/login')
def login(auth_details: AuthDetails):


    # check if user exists
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    # very user details and password & send token
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


# endpoint1
@app.get('/available_currency')
async def supported_currency_endpoint():
      result = {"supported currencies":"|EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand"}

      return result

# endpoint2
@app.post('/convert')
def convert(data:base_param,username=Depends(auth_handler.auth_wrapper)):
    date, rate, amnt = converter.convert(data.amount,data.from_currency, data.to_currency)
    result = {"Date":date, "Exchange Rate":rate, "Converted Amount":amnt,"Base currency":data.from_currency, "converted Currency":data.to_currency}
    
    data_f = pd.DataFrame({'user':username, 'log':str(result)}, index=[0])
    data_f.to_csv(config.LOG_CSV, mode='a', index=False, header=False)

    return {"result":result}

# logs endpoint
@app.get('/logs')
async def supported_currency_endpoint(username=Depends(auth_handler.auth_wrapper)):
      data  = pd.read_csv(config.LOG_CSV)
      result = data[data.user == str(username)]
      print(data.where(data['user'] == str('ian')))
      res = data.to_json()
      return {"result":res} 
      
if __name__ == '__main__':
      uvicorn.run(app, host=config.HOST, port=config.PORT)
from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from schema.schema import Convert
from db.database import Session, engine
from db.models import History
from converter import convert, availble_currencies
import datetime


# create db session 
session = Session(bind=engine)


# creatte crawler router instance for web crawler
convert_router = APIRouter(
      prefix='/convert',
      tags=['CONVERT']
)

#/api/v1/convert

# convert route
@convert_router.post('/convert' ,status_code=status.HTTP_200_OK)
async def conversion(convert_values: Convert, Authorize: AuthJWT=Depends()): 
      
      """
        ## convert currencies 
        This requires the following
        ```
                from_currency:str
                to_currency:str
                amount:float
        ```
        It requires an access token from login.
      """
      
      try:
            # request access token from authorized user
            Authorize.jwt_required()

      except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='unauthorized token')

      try:
            # convert currency with user defined parameters
            converted_values = convert(amount=convert_values.amount, base_currency=convert_values.from_currency,
                                          conv_currency=convert_values.to_currency)
      except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
            detail=str(e))
          
      current_user = Authorize.get_jwt_subject()

      print(converted_values)
      
      # record user conversion history to db
      new_history=History(
            username=current_user,
            price_date=converted_values['price_date'],
            from_currency=converted_values['from_currency'],
            to_currency=converted_values['to_currency'],
            exchange_rate=converted_values['exchange_rate'],
            converted_value=converted_values['converted_value'],
            date=datetime.datetime.now(datetime.timezone.utc)
      )
      session.add(new_history)

      session.commit()
      return {"results": converted_values }

# available currencies route
@convert_router.get('/currencies' ,status_code=status.HTTP_200_OK)
async def available_currencies(): 

      """
      ## available currencies
      This queries all currencies supported by API.
      """
      available = availble_currencies()
      
      return available


# history route 
@convert_router.get('/history' ,status_code=status.HTTP_200_OK)
async def history(Authorize: AuthJWT=Depends()): 

      """
      ## user crawl history
      This queries 10 latest instances a users conversion history from database. It requires a access token from login.
      """
      try:
            # request access token from authorized user
            Authorize.jwt_required()

      except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='unauthorized token')
      
      current_user = Authorize.get_jwt_subject()

      # query db for specific user's crawler history
      hist_data = session.query(History.date, History.price_date ,History.from_currency, History.to_currency, History.exchange_rate, History.converted_value).filter(History.username == current_user).all()

      return {f"history data for {current_user}": hist_data[:-10:-1]}
      
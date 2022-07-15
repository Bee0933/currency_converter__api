# **currency converter API 💲**

## ✔️ **Description** 📑
___
The aim of this project is to build real time currency converter API with the FastAPI Framework
<br><br>
This API workes by recieving the most recent currency exchange rate data using the [forex-python](https://forex-python.readthedocs.io/en/latest/index.html) library which provides free foreign exchange rates, bitcoin prices and currency conversion.

The API works with a list of currencies used world wide:

    EUR - Euro Member Countries |IDR - Indonesia Rupiah |BGN - Bulgaria Lev |ILS - Israel Shekel |GBP - United Kingdom Pound |DKK - Denmark Krone |CAD - Canada Dollar |JPY - Japan Yen |HUF - Hungary Forint |RON - Romania New Leu |MYR - Malaysia Ringgit |SEK - Sweden Krona |SGD - Singapore Dollar |HKD - Hong Kong Dollar |AUD - Australia Dollar |CHF - Switzerland Franc |KRW - Korea (South) Won |CNY - China Yuan Renminbi |TRY - Turkey Lira |HRK - Croatia Kuna |NZD - New Zealand Dollar |THB - Thailand Baht |USD - United States Dollar |NOK - Norway Krone |RUB - Russia Ruble |INR - India Rupee |MXN - Mexico Peso |CZK - Czech Republic Koruna |BRL - Brazil Real |PLN - Poland Zloty |PHP - Philippines Peso |ZAR - South Africa Rand


## **✔️ Run application**
setup virtual environment: <br>
`virtualenv shake`

activate virtual environment: <br>
`source shake/bin/activate`

install requirements to run application: <br>
`pip install -r requirements.txt`

run application: <br>
`uvicorn api:app --reload`

**curl comands to access API**

get list of all supported currencies: <br>
`curl -X 'GET' 'http://127.0.0.1:8000/available_currency' -H 'accept: application/json'` <br>
*! does not require authrntication*


register a new user: <br>
`curl -X 'POST' 'http://127.0.0.1:8000/register' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"username": "name","password": "pass"}'` <br>
*! does not require authrntication*


user login: <br>
`curl -X 'POST'  'http://127.0.0.1:8000/convert'  -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"amount": 500, "from_currency":"USD", "to_currency":"EUR"}' -H 'Authorization: Bearer <Token>`<br>
*! requires authentication*

view logs: <br>
`curl -X 'GET' 'http://127.0.0.1:8000/logs' -H 'Authorization: Bearer <Token>` <br>
*! requires authentication*


<!--  -->

## **✔️ Libraries and tools 🛠️**
___
<a href="https://www.python.org" target="_blank"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/git.png" height="50"> </a>
<a href="https://code.visualstudio.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png"/>
<img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png">
<img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg">
<img height="30" src="https://geekflare.com/wp-content/uploads/2019/07/fast-api-logo.png">
<img height="45" src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png"/>
<!--  -->

___
    * Python 3.8.10
    * FastAPI
    * Pandas
    * numpy
    * requests
    * uvicorn
    * forex-python

<!--  -->



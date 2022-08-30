# **currency converter API 💲**

## ✔️ **Description** 📑
___
The aim of this project is to build real time currency converter API with the FastAPI Framework
<br><br>
This API workes by recieving the most recent currency exchange rate data using the [forex-python](https://forex-python.readthedocs.io/en/latest/index.html) library which provides free foreign exchange rates, bitcoin prices and currency conversion.

The API works with a list of currencies used world wide:

___

## **✔️ Run application**

**Swagger API** <br>
[fastapi swagger](https://bee-currency.herokuapp.com/redoc) <br>
*! in debug mode*

___

### **curl comands to access API**

**get list of all supported currencies:** <br>
    
    curl -X 'GET' \
      'https://bee-currency.herokuapp.com/convert/currencies' \
      -H 'accept: application/json'

*! does not require authentication*

    output:

    { "available currencies": [
      "EUR",
      "JPY",
      "BGN",
      "CZK",
      "DKK", 
       ...
    }

<br>

**signin a new user:** 

    curl -X 'POST' \
      'https://bee-currency.herokuapp.com/auth/sign-in' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "username": "string",
      "email": "user@example.com",
      "password1": "string",
      "password2": "string"
      }'
*! does not require authentication*
  <br>

    output :

    { " message : "user registered" }




**user login:** 

    curl -X 'POST' \
      'https://bee-currency.herokuapp.com/auth/log-in' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{ 
      "email": "<user@example.com>",
      "password": "<string>"
      }' 

*! does not require authentication*

    output:

    {
      "access token": "xxxxxxxxxxxx",
      "refresh token": "xxxxxxxxxxxx"
    }

<br>



**get refresh token:** 

    curl -X 'GET' \
      'https://bee-currency.herokuapp.com/auth/refresh' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer <Token>

*! requires authentication which lasts for 10mins*

    output:

    {
      "access token": "xxxxxxxxxxxxxxxxxxx"
    }

<br>

**convert currencies:**

    curl -X 'POST' \
      'https://bee-currency.herokuapp.com/convert/convert' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer <Token> \
      -d '{ 
      "from_currency": "<EUR>", 
      "to_currency": "<INR>", 
      "amount": 0 
      }' 

*! requires authentication which lasts for 10mins*

    output:

    {
      "results": {
        "price_date": "29/08/2022",
        "from_currency": "EUR",
        "to_currency": "INR",
        "exchange_rate": 79.9025,
        "converted_value": 3196.1
      }
    }

<br>

**view conversion history:**

    curl -X 'GET' \
      'https://bee-currency.herokuapp.com/convert/history' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer <Token>

*! requires authentication which lasts for 10mins*

    output:

    {
      "history data for user": [
        {
          "date": "2022-08-29T14:47:31.433058",
          "price_date": "29/08/2022",
          "from_currency": "EUR",
          "to_currency": "INR",
          "exchange_rate": "79.9025",
          "converted_value": "3196.1"
        },
        {
          "date": "2022-08-29T14:47:19.603427",
          "price_date": "29/08/2022",
          "from_currency": "USD",
          "to_currency": "INR",
          "exchange_rate": "79.8466",
          "converted_value": "1596932.1475"
        },
        {
          "date": "2022-08-29T14:47:05.760249",
          "price_date": "29/08/2022",
          "from_currency": "USD",
          "to_currency": "PLN",
          "exchange_rate": "4.7452",
          "converted_value": "94903.5675"
        }
      ]
    }

<br>

<!--  -->

## **✔️ Libraries and tools 🛠️**
___
<a href="https://www.python.org" target="_blank"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/git.png" height="50"/> </a>
<a href="" target="_blank"> <img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png"></a>
<img height="45" src="https://api.iconify.design/simple-icons/fastapi.svg?color=%23059083&width=60&height=60"/>
<img height="45" src="https://api.iconify.design/logos/jwt-icon.svg?color=%23059083"/>
<img height="45" src="https://api.iconify.design/logos/gunicorn.svg"/>
<img height="45" src="https://api.iconify.design/logos/postgresql.svg"/>
<img height="50" src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png"/>
<img height="45" src="https://api.iconify.design/logos/heroku-icon.svg"/>
<!--  -->

___
    * Python 3.8.10
    * git
    * vscode
    * FastAPI
    * JWT
    * gunicorn
    * PostgreSQL
    * uvicorn
    * Heroku
    * psycobg2
    * requests
    * forex-python

<!--  -->

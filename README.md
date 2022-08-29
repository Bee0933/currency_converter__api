# **currency converter API 💲**

## ✔️ **Description** 📑
___
The aim of this project is to build real time currency converter API with the FastAPI Framework
<br><br>
This API workes by recieving the most recent currency exchange rate data using the [forex-python](https://forex-python.readthedocs.io/en/latest/index.html) library which provides free foreign exchange rates, bitcoin prices and currency conversion.

The API works with a list of currencies used world wide:


## **✔️ Run application**

**Swagger API**
[fastapi swagger](https://bee-currency.herokuapp.com/docs) <br>
*! in debug mode*

**curl comands to access API**

get list of all supported currencies: <br>
`curl -X 'GET' 'https://bee-currency.herokuapp.com/convert/currencies' -H 'accept: application/json'` <br>
*! does not require authentication*

signin a new user: <br>
`curl -X 'POST' 'https://bee-currency.herokuapp.com/auth/sign-in' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "username": "<string>", "email": "<user@example.com>", "password": "<string>", "confirm password": "<string>"}'` <br>
*! does not require authrntication*

user login: <br>
`curl -X 'POST' 'https://bee-currency.herokuapp.com/auth/log-in' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "email": "<user@example.com>","password": "<string>"}'`<br>
*! does not require authentication*

get refresh token: <br>
`curl -X 'GET' 'https://bee-currency.herokuapp.com/auth/refresh' -H 'accept: application/json' -H 'Authorization: Bearer <Token>`
*! requires authentication which lasts for 10mins*

convert currencies: <br>
`curl -X 'POST' 'https://bee-currency.herokuapp.com/convert/convert' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{ "from_currency": "<USD>", "to_currency": "<EUR>", "amount": 0 }' H 'Authorization: Bearer <Token>`

view conversion history: <br>
`curl -X 'GET' 'https://bee-currency.herokuapp.com/convert/history' -H 'accept: application/json' -H 'Authorization: Bearer <Token>` <br>
*! requires authentication which lasts for 10mins*

<br>

<!--  -->

## **✔️ Libraries and tools 🛠️**
___
<a href="https://www.python.org" target="_blank"> <img src="https://img.icons8.com/color/48/000000/python.png"/> </a>
<a href="https://git-scm.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/git.png" height="50"> </a>
<a href="https://code.visualstudio.com/" target="_blank"> <img src="https://img.icons8.com/color/48/000000/visual-studio-code-2019.png"/>
<img height="30" src="https://geekflare.com/wp-content/uploads/2019/07/fast-api-logo.png">
<img height="45" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS24iIQUg5hYsYyFavhPKXQJuXstAUjWt6maNYu-wWE6240yxhxDulIejacyWqidzwT2w&usqp=CAU"/>
<img height="45" src="https://w7.pngwing.com/pngs/358/849/png-transparent-postgresql-database-logo-database-symbol-blue-text-logo-thumbnail.png"/>
<img height="45" src="https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png"/>
<!--  -->

___
    * Python 3.8.10
    * FastAPI
    * PostgreSQL
    * psycobg2
    * requests
    * gunicorn
    * uvicorn
    * JWT Auth
    * forex-python

<!--  -->



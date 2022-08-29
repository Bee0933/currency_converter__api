from typing import Optional
from pydantic import BaseModel, Field, EmailStr, StrictBool, validator
from decouple import config
from enum import Enum


# sign-in end-point schema
class signUser(BaseModel):
      username : str = Field(default=None, max_length=30, description="user unique name")
      email : EmailStr = Field(default=None, description='user email for log-in')
      password1 : str = Field(default=None, description='user password for log-in')
      password2 : str = Field(default=None, description='confirm user password')

      @validator('password2')
      def passwords_match(cls, v, values, **kwargs):
            if 'password1' in values and v != values['password1']:
                  raise ValueError('passwords do not match')
            return v
      class config:
            orm_mode=True
            schema_extra = {
                  "username" : "<username>",
                  "email" : "<user@email.com>",
                  "password" : "<password>",
            }

# log-in end-point schema 
class logUser(BaseModel):
      email : EmailStr = Field(default=None, description='user email to log-in')
      password : str = Field(default=None, description='user password for log-in')
      class config:
            orm_mode=True
            schema_extra = {
                  "email" : "<user@email.com>",
                  "password" : "<password>",
            }

# convert currency schema
class Convert(BaseModel):
      from_currency : str = Field(default=None, description='base/initial currency code')
      to_currency : str = Field(default=None, description='final/converted currency code')
      amount : float = Field(default=None, gt=1,  description='numerical value to be converted')
            
# jwt auth
class Settings(BaseModel):
      authjwt_secret_key : str = config('secret')
from fastapi import APIRouter, status, Depends
from db.database import Session, engine
from schema.schema import signUser, logUser
from db.models import User
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash , check_password_hash
from fastapi_jwt_auth import AuthJWT 
from fastapi.encoders import jsonable_encoder

# create auth router instance for sig-nup and log-in  
auth_router = APIRouter(
      prefix='/auth',
      tags=['AUTH']
)

session = Session(bind=engine)

@auth_router.post('/sign-in', status_code=status.HTTP_201_CREATED)
async def sigin(user:signUser):

      """
        ## Sign-in a user
        This requires the following
        ```
                username:int
                email:EmailStr
                password1:str
                password2:str
        ```
    """
      # query db if email exists 
      db_email = session.query(User).filter(User.email==user.email).first()
      
      if db_email is not None:
            return HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST,
                  detail='user email already exists')

      # query db if username exists
      db_username = session.query(User).filter(User.username==user.username).first()
      
      if db_username is not None:
            return HTTPException(
                  status_code=status.HTTP_400_BAD_REQUEST,
                  detail='username already exists')
      
      # create new user to ingest to database
      new_user=User(
            username=user.username,
            email=user.email,
            password=generate_password_hash(user.password1)
      )

      session.add(new_user)

      session.commit()
      return f'{user.username} registered!'



# login route 
@auth_router.post('/log-in')
async def login(user : logUser, Authorize:AuthJWT=Depends()):
      
      """
        ## login a user
        This requires the following
        ```
                email:EmailStr
                password:str   
        ```
      """
      # query db if user exists
      db_user = session.query(User).filter(User.email == user.email).first()

      if db_user and check_password_hash(db_user.password, user.password):
            
            #create jwt access token for authorized user
            access_token=Authorize.create_access_token(subject=db_user.username)
            
            # create refresh token for authorized user 
            refresh_token=Authorize.create_refresh_token(subject=db_user.username)
            
            # output response
            response = {
                  "access token": access_token,
                  "refresh token": refresh_token
            }
            return jsonable_encoder(response)
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Invalid email or password')


# refresh route
@auth_router.get('/refresh', status_code=status.HTTP_201_CREATED)
async def refresh(Authorize:AuthJWT=Depends()):
      
      """
      ## Create a new token
      This creates a new token. It requires a refresh token from login.
      """
      try:
            # request access token from authorized user
            Authorize.jwt_refresh_token_required()
      
      except Exception as e:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail='please provide a valid refresh token')
      
      current_user = Authorize.get_jwt_subject()
      # print('current_user:', current_user)

      # create new token for authorized user
      access_token = Authorize.create_access_token(subject=current_user)

      return jsonable_encoder({"access token":access_token})
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.database import Base


# user table 
class User(Base):
      __tablename__ = 'user'
      id=Column(Integer, primary_key=True)
      username=Column(String(50), unique=True, nullable=False)
      email=Column(String(30), nullable=False)
      password=Column(String(200), nullable=False)

      def __repr__(self) -> str:
            return f'user: {self.username}, email : {self.email}'

# history table 
class History(Base):
      __tablename__ = 'history'
      id = Column(Integer,primary_key=True)
      username=Column(String(30), nullable=False, unique=False)
      price_date=Column(String(30), nullable=False)
      from_currency=Column(String(4), nullable=False)
      to_currency=Column(String(4), nullable=False)
      exchange_rate=Column(String(30), nullable=False)
      converted_value=Column(String(30), nullable=False)
      date=Column(DateTime(), nullable=False)

      def __repr__(self):
            return f'<History id {self.id}'
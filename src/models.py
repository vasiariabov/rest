from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class User(Base):
    __tablename__ = "task"    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String(255))
    done = Column(String(50))

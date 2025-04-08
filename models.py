from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Bank(Base):
    __tablename__ = 'banks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    branches = relationship("Branch", back_populates="bank")

class Branch(Base):
    __tablename__ = 'branches'
    ifsc = Column(String, primary_key=True)
    branch = Column(String)
    address = Column(String)
    city = Column(String)
    district = Column(String)
    state = Column(String)
    bank_id = Column(Integer, ForeignKey('banks.id'))
    bank = relationship("Bank", back_populates="branches")
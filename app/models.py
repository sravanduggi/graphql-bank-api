from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from typing import List

Base = declarative_base()

class Bank(Base):
    """Bank model representing a banking institution."""
    __tablename__ = 'banks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    branches = relationship("Branch", back_populates="bank", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Bank(id={self.id}, name='{self.name}')>"

class Branch(Base):
    """Branch model representing a bank branch location."""
    __tablename__ = 'branches'

    ifsc = Column(String(11), primary_key=True, index=True)
    branch = Column(String(100), nullable=True)
    address = Column(String(200), nullable=True)
    city = Column(String(50), nullable=True, index=True)
    district = Column(String(50), nullable=True, index=True)
    state = Column(String(50), nullable=True, index=True)
    bank_id = Column(Integer, ForeignKey('banks.id', ondelete='CASCADE'), nullable=False)
    
    bank = relationship("Bank", back_populates="branches")

    def __repr__(self) -> str:
        return f"<Branch(ifsc='{self.ifsc}', branch='{self.branch}', city='{self.city}')>" 
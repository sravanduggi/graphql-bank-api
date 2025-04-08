import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from models import Bank, Branch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@strawberry.type
class BankType:
    id: int
    name: str

@strawberry.type
class BranchType:
    ifsc: str
    bank: BankType
    branch: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None

@strawberry.type
class BranchEdge:
    node: BranchType

@strawberry.type
class BranchConnection:
    edges: List[BranchEdge]

@strawberry.type
class Query:
    @strawberry.field
    def branches(self) -> BranchConnection:
        db = SessionLocal()
        try:
            branches = db.query(Branch).all()
            edges = [
                BranchEdge(
                    node=BranchType(
                        ifsc=branch.ifsc,
                        branch=branch.branch,
                        address=branch.address,
                        city=branch.city,
                        district=branch.district,
                        state=branch.state,
                        bank=BankType(
                            id=branch.bank.id,
                            name=branch.bank.name
                        )
                    )
                )
                for branch in branches
            ]
            return BranchConnection(edges=edges)
        finally:
            db.close()

schema = strawberry.Schema(query=Query)
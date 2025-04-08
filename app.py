
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import schema

# Create FastAPI app
app = FastAPI(title="Bank Branches API")

# Database setup
DATABASE_URL = "sqlite:///bank.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# GraphQL setup
graphql_app = GraphQLRouter(schema)

# Add GraphQL route
app.include_router(graphql_app, prefix="/gql")

@app.get("/")
async def root():
    return {"message": "Welcome to Bank Branches API. Use /gql for GraphQL queries"}
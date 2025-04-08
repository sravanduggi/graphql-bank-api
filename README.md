# Indian Bank Branches GraphQL API

A modern GraphQL API service for querying Indian bank branch information, built with FastAPI and Strawberry GraphQL.

## Overview

This API provides access to Indian bank branch information through a GraphQL interface. The data includes comprehensive details about bank branches across India.

### Features

- GraphQL API with Strawberry GraphQL
- SQLite database with bank and branch information
- Full-text search capabilities
- Comprehensive API documentation
- Test coverage
- Production-ready setup

## Tech Stack

- **Framework**: FastAPI
- **GraphQL**: Strawberry GraphQL
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package manager)

### Installation

1. Clone the repository:
```powershell
git clone <repository-url>
cd bank-branches-api
```

2. Create and activate virtual environment:
```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Seed the database:
```powershell
python seed_db.py
```

5. Run the application:
```powershell
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoints

- **GraphQL Playground**: `http://localhost:8000/gql`

### Example GraphQL Query

```graphql
query {
  branches {
    edges {
      node {
        ifsc
        branch
        city
        state
        bank {
          name
        }
      }
    }
  }
}
```

## Testing

Run tests using:
```powershell
python -m pytest test_app.py -v
```


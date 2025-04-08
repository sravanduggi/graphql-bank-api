from fastapi.testclient import TestClient
import pytest
from app import app

# Create test client
client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Bank Branches API. Use /gql for GraphQL queries"}

def test_graphql_branches_query():
    query = """
    query {
        branches {
            edges {
                node {
                    branch
                    bank {
                        name
                    }
                    ifsc
                }
            }
        }
    }
    """
    response = client.post("/gql", json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "branches" in data["data"]
    assert "edges" in data["data"]["branches"]
    
    # Verify the structure of the response
    edges = data["data"]["branches"]["edges"]
    assert isinstance(edges, list)
    if edges:  # If there are any branches in the database
        first_edge = edges[0]
        assert "node" in first_edge
        node = first_edge["node"]
        assert "branch" in node
        assert "bank" in node
        assert "ifsc" in node
        assert "name" in node["bank"] 
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///bank.db')
Base.metadata.create_all(engine)
db_session = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

app.add_url_rule(
    '/gql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)



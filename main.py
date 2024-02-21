from fastapi import FastAPI, Depends
from strawberry.fastapi import GraphQLRouter
from StrawberryGQL.GQL import schema
from MongoDB import NoSQL
from RedisCache import Cache

# Base.metadata.create_all(bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Annotated[Session, Depends(get_db)]

#Creating an instance of Redis
redis = Cache()

#Creating an instance of MongoDB
mongoDB = NoSQL()

#Creating an instance of a FastAPI Application
app = FastAPI()

#Creating an instance of a FastAPI Application
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")

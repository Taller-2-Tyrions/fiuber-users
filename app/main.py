from fastapi import FastAPI
from routers import users
from models import users as models
from database.database import engine


app = FastAPI()

# no deberia estar porque lo hace otro coso. 
models.Base.metadata.create_all(engine)


app.include_router(users.router)

@app.get("/")
async def root():
    return {"Hello": "World"}

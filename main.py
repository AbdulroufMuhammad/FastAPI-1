from fastapi import FastAPI
from db import model
from db.database import engine
from db import user
from db.routes import ArticleRoute
app = FastAPI()

app.include_router(user.router)
app.include_router(ArticleRoute.router)

@app.get('/')
def Home():
    return 'Home'


model.Base.metadata.create_all(engine)
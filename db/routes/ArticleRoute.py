from fastapi import APIRouter,Depends
from schema import ArticleDisplay,ArticleBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import ArticleCreate

router = APIRouter(
    prefix= '/Article',
    tags= ['Articles']
)

# Create
@router.post('/',response_model= ArticleDisplay)
def CreateArticle(request: ArticleBase, db: Session = Depends(get_db)):
    return ArticleCreate.CreateArticle(db,request)

# Read
@router.get('/{id}')
def getArticle(id: int,db:Session = Depends(get_db)):
    return ArticleCreate.getArticle(id,db)
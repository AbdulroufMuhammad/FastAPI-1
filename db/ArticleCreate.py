from sqlalchemy.orm import Session
from schema import ArticleBase
from db.model import ArticleTable
from typing import List

def CreateArticle(db: Session, request:ArticleBase):
    NewArticle = ArticleTable(
        Title = request.Title,
        Content = request.Content,
        Published = request.Published,
        Creator_id = request.Creator_id
    )
    db.add(NewArticle)
    db.commit()
    db.refresh(NewArticle)
    return NewArticle

def getArticle(id:int, db:Session):
    article = db.query(ArticleTable).filter(ArticleTable.id == id).first()
    return article
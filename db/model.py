from db.database import Base
from sqlalchemy import Column,Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship
class Db_table(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True)
    UserName = Column(String)
    Email = Column(String)
    Password = Column(String)
    Items = relationship('ArticleTable',back_populates='User')

class ArticleTable(Base):
    __tablename__ = "Articles"

    id = Column(Integer,primary_key=True)
    Title = Column(String)
    Content = Column(String)
    Published = Column(Boolean)
    Creator_id = Column(Integer,ForeignKey('data.id'))
    User = relationship('Db_table',back_populates='Items')

from pydantic import BaseModel
from typing import List
        
class CreateuserBase(BaseModel):
    UserName : str
    Email : str
    Password : str

class Article(BaseModel):
    Title : str
    Content : str
    Published : bool
    class Config():
        orm_mode = True
    
class Userr(BaseModel):
    id : int
    UserName : str
    class Config():
        orm_mode = True


class UserDisplay(BaseModel):
    UserName : str
    Email : str
    Items : List[Article] = []
    class Config():
        orm_mode = True

class ArticleBase(BaseModel):
    Title : str
    Content : str
    Published : bool
    Creator_id: int

class ArticleDisplay(BaseModel):
    Title : str
    Content : str
    Published : bool
    User : Userr
    class Config():
        orm_mode = True


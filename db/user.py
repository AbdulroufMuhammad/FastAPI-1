from fastapi import APIRouter,Depends,Body
from sqlalchemy.orm.session import Session
from db.database import get_db
from schema import CreateuserBase,UserDisplay
from db import userCreate

router = APIRouter(
    prefix= '/user',
    tags= ['user']
)

# Create
@router.post('/create', response_model = UserDisplay)
def user(request: CreateuserBase, db:Session = Depends(get_db)):
    return userCreate.Create_user(db, request)



# Read 
@router.get('/ReadAll',response_model=UserDisplay)
def Read(db:Session = Depends(get_db)):
    return userCreate.Read_All(db)

#  Readby_id
@router.get('/{id}/ReadById',response_model=UserDisplay)
def ReadBy_id(id:int,db:Session = Depends(get_db)):
    return userCreate.Read_by_Id(id, db)

# Update
@router.post('/{id}/update')
def UpdateUser(id: int, request: CreateuserBase, db:Session = Depends(get_db)):
    return userCreate.Update_Data(db, id, request)
# Delete
@router.get('/{id}/Delete')
def Delete(id:int, db:Session = Depends(get_db)):
    return userCreate.delete(id,db)
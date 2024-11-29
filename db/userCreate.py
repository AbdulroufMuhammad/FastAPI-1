from sqlalchemy.orm.session import Session
from schema import CreateuserBase
from db.model import Db_table
from db.hash import Hash


# Create
def Create_user(db: Session, request: CreateuserBase):
    NewUser = Db_table(
        UserName=request.UserName,
        Email=request.Email,
        Password=Hash.bcrypt(request.Password)
    )
    db.add(NewUser)
    db.commit()
    db.refresh(NewUser)
    return NewUser

# Read
def Read_All(db:Session):
    return db.query(Db_table).all()

# Read_by_id

def Read_by_Id(id: int,db:Session):
    user = db.query(Db_table).filter(Db_table.id == id).first()
    return user

# Update
def Update_Data(db:Session,id:int, request:CreateuserBase):
    user = db.query(Db_table).filter(Db_table.id == id)
    user.update({
        Db_table.UserName: request.UserName,
        Db_table.Email: request.Email,
        Db_table.Password: Hash.bcrypt(request.Password)
    })
    db.commit()
    return ' updated'
# Delete
def delete(id:int, db:Session):
    user = db.query(Db_table).filter(Db_table.id == id).first()
    db.delete(user)
    db.commit()
    return 'User Deleted'


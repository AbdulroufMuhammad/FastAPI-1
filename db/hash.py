from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes='bcrypt',deprecated = 'auto')


class Hash:
    def bcrypt(Password: str):
        return pwd_cxt.hash(Password)
    
    def Verify(hashed_password,plain_password):
        return pwd_cxt.verify(hashed_password,plain_password)
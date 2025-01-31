import jwt
import datetime
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from config import config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


class AuthService:
    @staticmethod
    def create_access_token(user_id: str):
        """ Generates JWT Token """
        expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": user_id, "exp": expiration}
        token = jwt.encode(payload, config.SECRET_KEY, algorithm=config.ALGORITHM)
        return token

    @staticmethod


    def verify_token(token: str = Depends(oauth2_scheme)):
        """ Verifies JWT Token """
        try:
            payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

auth_service = AuthService()

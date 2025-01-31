from fastapi import APIRouter, Depends
from services.auth_service import auth_service

router = APIRouter()


@router.post("/token")
def generate_token():
    token = auth_service.create_access_token(user_id="user123")
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def get_current_user(user: dict = Depends(auth_service.verify_token)):
    return {"user": user}

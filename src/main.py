from fastapi import FastAPI
from routes import gateway, auth

app = FastAPI(title="FastAPI Gateway")

app.include_router(auth.router, prefix="/auth")
app.include_router(gateway.router, prefix="/api")


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Gateway"}

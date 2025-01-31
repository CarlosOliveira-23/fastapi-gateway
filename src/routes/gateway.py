from fastapi import APIRouter, HTTPException
import httpx
from fastapi.responses import JSONResponse


MICROSERVICES = {
    "service1": "http://localhost:5001",
    "service2": "http://localhost:5002",
}

router = APIRouter()


@router.get("/api/{service}/{path:path}")
async def proxy_request(service: str, path: str):
    if service not in MICROSERVICES:
        raise HTTPException(status_code=404, detail="Service not found")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{MICROSERVICES[service]}/{path}")
        return JSONResponse(content=response.json(), status_code=response.status_code)

import aioredis
from fastapi import Request, HTTPException
from config import config

redis = None


async def init_redis():
    global redis
    redis = await aioredis.from_url(f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}")


async def rate_limit_middleware(request: Request, call_next):
    if not redis:
        await init_redis()

    ip = request.client.host
    key = f"ratelimit:{ip}"
    requests = await redis.incr(key)

    if requests == 1:
        await redis.expire(key, 60)

    if requests > 10:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    response = await call_next(request)
    return response

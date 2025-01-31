import aioredis
from fastapi import Request
from config import config

redis = None


async def init_redis():
    global redis
    redis = await aioredis.from_url(f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}")


async def caching_middleware(request: Request, call_next):
    if not redis:
        await init_redis()

    cache_key = f"cache:{request.url.path}"
    cached_response = await redis.get(cache_key)

    if cached_response:
        return cached_response

    response = await call_next(request)
    await redis.set(cache_key, response.body, ex=60)

    return response

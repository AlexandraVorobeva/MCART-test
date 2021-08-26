import uvicorn
from fastapi import FastAPI
from .routs import router
import os
from fastapi import Request, Response

from fastapi_redis_cache import FastApiRedisCache, cache

app = FastAPI(title="MCART", description="API by Aexandra Vorobeva")
app.include_router(router)


LOCAL_REDIS_URL = "redis://127.0.0.1:6379"


@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=os.environ.get("REDIS_URL", LOCAL_REDIS_URL),
        prefix="myapi-cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response]
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

import uvicorn
from fastapi import FastAPI
from .routs import router


app = FastAPI(title="MCART", description="API by Aexandra Vorobeva")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

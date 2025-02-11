from fastapi import FastAPI
from app.api import api

app = FastAPI()

@app.on_event("startup")
async def startup():
    pass

app.include_router(api.api_router)
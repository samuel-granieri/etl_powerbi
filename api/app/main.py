from fastapi import FastAPI
from app.routes import rotas

app = FastAPI(title="Gold API")

app.include_router(rotas.router)
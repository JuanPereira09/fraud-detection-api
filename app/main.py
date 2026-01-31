from fastapi import FastAPI
from app.routes import fraud
from app.database import engine
from app.models.transaction import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fraud Detection API")

app.include_router(fraud.router)

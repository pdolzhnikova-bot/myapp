from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/db-url")
def db_url() -> dict[str, str]:
    return {"database_url": os.getenv("DATABASE_URL", "not set")}

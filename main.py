from fastapi import FastAPI
from database import start_db
from routers.species import router as species_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
def on_startup():
    start_db()

app.include_router(species_router)
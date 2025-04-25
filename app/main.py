from fastapi import FastAPI
from .routes import events
from .database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Ubatuba Events API",
    description="API for managing events in Ubatuba, São Paulo",
    version="1.0.0"
)

app.include_router(events.router) 
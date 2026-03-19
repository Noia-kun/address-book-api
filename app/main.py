import logging
from fastapi import FastAPI
from . import models, database
from .routers import addresses

# 1. Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# 2. Create Database Tables
# This command tells SQLAlchemy to create the .db file and tables
# if they don't already exist.
models.Base.metadata.create_all(bind=database.engine)

# 3. Initialize FastAPI
app = FastAPI(
    title="Address Book API",
    description="A minimal API to manage addresses and calculate distances.",
    version="1.0.0"
)

# 4. Include Routers
app.include_router(addresses.router)

@app.get("/")
async def root():
    """Welcome endpoint to verify the API is running."""
    logger.info("Root endpoint accessed")
    return {
        "message": "Welcome to the Address Book API",
        "docs": "/docs",
        "status": "online"
    }
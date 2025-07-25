"""Main FastAPI application module for the agent-template-repo API."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.endpoints.search import router as search_router

app = FastAPI(title="Agent Test API",
              description="A standard FastAPI application",
              version="0.1.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(search_router, prefix="/api/v1", tags=["search"])


@app.get("/")
async def root():
    """Return a simple greeting message.
    
    Returns:
        A dictionary containing a greeting message.
    """
    return {"message": "Hello from agent-template-repo!"}


@app.get("/health")
async def health_check():
    """Check the health status of the API.
    
    Returns:
        A dictionary indicating the API is healthy.
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

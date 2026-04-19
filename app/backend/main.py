"""FastAPI backend for the AI Hedge Fund application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="AI Hedge Fund API",
    description="Backend API for the AI-powered hedge fund simulation",
    version="0.1.0",
)

# Allow frontend dev server and production origins
# Added 8080 since I sometimes run the frontend on that port locally
# Added 4173 for vite preview mode
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:8080", "http://localhost:4173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.get("/")
async def root():
    """Root endpoint with basic API info."""
    return {
        "name": "AI Hedge Fund API",
        "version": "0.1.0",
        "docs": "/docs",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

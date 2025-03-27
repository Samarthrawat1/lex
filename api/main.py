from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from routes import logs, health
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Lex - Log Exposition Service API"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["health"])
app.include_router(logs.router, prefix="/api/v1", tags=["logs"])

@app.get("/")
def read_root():
    # Might not follow the roadmap :p
    return r"Life's a journey, Clark. I don't want to go through it following a roadmap. -Lex Luthor"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

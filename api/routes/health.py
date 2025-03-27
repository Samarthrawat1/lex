from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Basic health check endpoint to verify API is running.
    """
    return {
        "status": "healthy",
        "service": "lex-api"
    } 
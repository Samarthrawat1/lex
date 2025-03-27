from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Lex"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # CORS
    ALLOWED_ORIGINS: List[str]
    
    # MongoDB
    MONGODB_URL: str
    MONGODB_DB_NAME: str
    
    # Redis
    REDIS_URL: str
    
    # Single admin API key
    ADMIN_API_KEY: str
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 
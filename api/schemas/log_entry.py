from datetime import datetime
from typing import Dict, Optional, Union
from enum import Enum
from pydantic import BaseModel, Field, field_validator

class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class LogMetadata(BaseModel):
    """Additional contextual information about the log entry"""
    service: str = Field(..., description="Name of the service generating the log")
    environment: str = Field(..., description="Environment (e.g., prod, staging, dev)")
    host: Optional[str] = Field(None, description="Hostname or container ID")
    trace_id: Optional[str] = Field(None, description="Distributed tracing ID")
    custom_fields: Dict[str, Union[str, int, float, bool]] = Field(
        default_factory=dict,
        description="Additional custom key-value pairs"
    )

class LogEntry(BaseModel):
    """
    Standard log entry format for the Lex logging system.
    All timestamps are stored in UTC.
    """
    id: Optional[str] = Field(None, description="Unique identifier for the log entry")
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="UTC timestamp of the log event"
    )
    level: LogLevel = Field(..., description="Severity level of the log")
    message: str = Field(..., description="Main log message")
    source: str = Field(..., description="Source of the log (application name/component)")
    metadata: LogMetadata = Field(..., description="Additional contextual information")

    @field_validator('message')
    @classmethod
    def message_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError('Message cannot be empty or just whitespace')
        return v.strip()

    class Config:
        json_schema_extra = {
            "example": {
                "timestamp": "2024-03-20T15:30:00Z",
                "level": "ERROR",
                "message": "Database connection failed",
                "source": "user-service",
                "metadata": {
                    "service": "user-service",
                    "environment": "production",
                    "host": "web-server-01",
                    "trace_id": "abc123xyz789",
                    "custom_fields": {
                        "user_id": "12345",
                        "request_duration_ms": 1500,
                        "endpoint": "/api/users"
                    }
                }
            }
        } 
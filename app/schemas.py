from pydantic import BaseModel
from typing import Generic, TypeVar, Optional, Any

T = TypeVar("T")

class ResponseSchema(BaseModel, Generic[T]):
    status: str = "success"
    message: str = "Request processed successfully"
    data: Optional[T] = None

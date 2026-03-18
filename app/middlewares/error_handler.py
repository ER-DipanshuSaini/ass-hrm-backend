from fastapi import Request
from fastapi.responses import JSONResponse
import logging

async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Global Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Internal Server Error", "data": str(exc)}
    )

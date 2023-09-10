#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI
from config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url="/openapi",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    debugger=True
)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT
    )

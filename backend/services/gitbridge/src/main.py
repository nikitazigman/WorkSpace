import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.settings.application import get_app_settings
from src.api.v1 import github
from contextlib import asynccontextmanager
from loguru import logger


settings = get_app_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    try:
        # TODO: define redis async client
        # TODO: define rabbit async client
        # TODO: define postgres async client
        yield
        # TODO: close redis async client
        # TODO: close rabbit async client
        # TODO: close postgres async client
    finally:
        logger.warning("Shutting down...")


app = FastAPI(
    lifespan=lifespan,
    title="GitBridge",
    description="A simple service to bridge GitHub webhooks to WorkSpace.",
    version="0.0.1",
    default_response_class=ORJSONResponse,
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
)

app.include_router(github.router, prefix="/api/v1/github", tags=["github"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
        log_level="debug" if settings.debug else "info",
    )

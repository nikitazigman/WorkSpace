import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.settings.application import get_app_settings
from src.api.v1 import github
from src.db import rabbitmq
from contextlib import asynccontextmanager
from loguru import logger


settings = get_app_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up...")
    try:
        await rabbitmq.establish_connection()
        await rabbitmq.declare_exchange()
        yield
        await rabbitmq.close_connection()
    finally:
        logger.warning("Shutting down...")


app = FastAPI(
    lifespan=lifespan,
    version="0.0.1",
    title="GitBridge",
    description="Service to bridge GitHub webhooks to WorkSpace.",
)


app_v1 = FastAPI(
    title="GitBridge API V1",
    version="0.0.1",
    default_response_class=ORJSONResponse,
    docs_url="/docs",
    root_path="/api/v1",
)


app_v1.include_router(github.router, prefix="/github", tags=["github"])

app.mount(app_v1.root_path, app_v1, name="v1")
app.openapi_tags = [
    {
        "name": "v1",
        "externalDocs": {
            "description": "V1 docs",
            "url": f"http://{settings.app_host}:{settings.app_port}{app_v1.root_path}{app_v1.docs_url}",
        },
    },
]

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=settings.debug,
        log_level="debug" if settings.debug else "info",
    )

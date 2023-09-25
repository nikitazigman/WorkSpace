from abc import ABC, abstractmethod
from src.db.rabbitmq import IPublisher, get_publisher
from loguru import logger
from src.utils.transformers import (
    ITransformer,
    PayloadType,
    get_github_issue_transformer,
    get_github_pull_request_transformer,
)

from typing import Generic, Annotated
from functools import lru_cache
from fastapi import Depends
from src.schemas.responses import BaseResponse


class IGitHubWebhookService(ABC, Generic[PayloadType]):
    @abstractmethod
    async def handle_webhook_payload(
        self,
        secret_key: str,
        payload: PayloadType,
    ) -> BaseResponse:
        ...


class GitHubWebhookService(IGitHubWebhookService, Generic[PayloadType]):
    def __init__(self, publisher: IPublisher, transformer: ITransformer):
        self.publisher = publisher
        self.transformer = transformer

    def validate_secret_key(self, secret_key: str):
        logger.info("secret key is valid")

    async def handle_webhook_payload(
        self,
        secret_key: str,
        payload: PayloadType,
    ) -> BaseResponse:
        logger.info(f"handling webhook payload: {payload=}")
        self.validate_secret_key(secret_key)
        task = self.transformer.transform(payload)
        await self.publisher.publish(task)
        return BaseResponse()


@lru_cache(maxsize=1)
def get_github_issue_webhook_service(
    publisher: Annotated[IPublisher, Depends(get_publisher)],
    transformer: Annotated[ITransformer, Depends(get_github_issue_transformer)],
) -> IGitHubWebhookService:
    return GitHubWebhookService(publisher=publisher, transformer=transformer)


@lru_cache(maxsize=1)
def get_github_pull_request_webhook_service(
    publisher: Annotated[IPublisher, Depends(get_publisher)],
    transformer: Annotated[ITransformer, Depends(get_github_pull_request_transformer)],
) -> IGitHubWebhookService:
    return GitHubWebhookService(publisher=publisher, transformer=transformer)

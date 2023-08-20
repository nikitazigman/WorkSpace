from abc import ABC, abstractmethod
from src.utils.publishers import IPublisher, DPublisher
from loguru import logger
from src.utils.transformers import (
    ITransformer,
    DIssueTransformer,
    DPullRequestTransformer,
)
from src.utils.validators import ISecretValidator, DValidator
from src.utils.user_repositories import IUserRepo, DUserRepo
from typing import Annotated
from functools import lru_cache
from fastapi import Depends
from src.schemas.responses import BaseResponse
from uuid import UUID


class IGitHubBridgeService(ABC):
    @abstractmethod
    async def handle_webhook_payload(
        self, signature: str, payload_bytes: bytes, user_id: UUID
    ) -> BaseResponse:
        """Handle webhook payload from GitHub.

        Args:
            signature: signature header from GitHub
            payload_bytes: payload body from GitHub
            user_id: user id from WorkSpace UserAPI
        Returns:
            BaseResponse: response with status code 200
        """


class GitHubBridgeService(IGitHubBridgeService):
    def __init__(
        self,
        publisher: IPublisher,
        transformer: ITransformer,
        validator: ISecretValidator,
        user_repo: IUserRepo,
    ):
        self.publisher = publisher
        self.transformer = transformer
        self.validator = validator
        self.user_repo = user_repo

    async def handle_webhook_payload(
        self, signature: str, payload_bytes: bytes, user_id: UUID
    ) -> BaseResponse:
        logger.info("handling webhook payload...")

        user = await self.user_repo.get_user(user_id)
        await self.validator.verify_signature(payload_bytes, user.secret_key, signature)
        task = self.transformer.transform(payload_bytes, user.id)
        await self.publisher.publish(task)

        return BaseResponse()


@lru_cache(maxsize=1)
def get_github_issue_webhook_service(
    publisher: DPublisher,
    transformer: DIssueTransformer,
    validator: DValidator,
    user_repo: DUserRepo,
) -> IGitHubBridgeService:
    return GitHubBridgeService(
        publisher=publisher,
        transformer=transformer,
        validator=validator,
        user_repo=user_repo,
    )


@lru_cache(maxsize=1)
def get_github_pull_request_webhook_service(
    publisher: DPublisher,
    transformer: DPullRequestTransformer,
    validator: DValidator,
    user_repo: DUserRepo,
) -> IGitHubBridgeService:
    return GitHubBridgeService(
        publisher=publisher,
        transformer=transformer,
        validator=validator,
        user_repo=user_repo,
    )


DGitHubIssueWebhookService = Annotated[
    GitHubBridgeService,
    Depends(get_github_issue_webhook_service),
]
DGitHubPullRequestWebhookService = Annotated[
    GitHubBridgeService,
    Depends(get_github_pull_request_webhook_service),
]

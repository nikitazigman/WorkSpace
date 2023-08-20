from abc import ABC, abstractmethod
from src.schemas.tasks import Task, TaskType, SourceType
from src.schemas.github import (
    GitHubIssuePayload,
    GitHubPullRequestPayload,
    GitHubCommonPayload,
)
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from uuid import UUID
from loguru import logger


class ITransformer(ABC):
    @abstractmethod
    def transform(self, payload: bytes, user_id: UUID) -> Task:
        ...


class GitHubIssueTransformer(ITransformer):
    def transform(self, payload: bytes, user_id: UUID) -> Task:
        logger.debug("Transforming GitHubIssuePayload to Task...")
        issue_payload = GitHubIssuePayload.model_validate_json(payload)
        return Task(
            event_type=TaskType.ISSUE,
            source_type=SourceType.GITHUB,
            user_id=user_id,
            url=issue_payload.issue.url,
            title=issue_payload.issue.title,
            body=issue_payload.issue.body,
            created_at=issue_payload.issue.created_at,
            updated_at=issue_payload.issue.updated_at,
        )


# TODO: Implement GitHubPullRequestTransformer
class GitHubPullRequestTransformer(ITransformer):
    def transform(self, payload: bytes, user_id: UUID) -> Task:
        logger.debug("Transforming GitHubPullRequestPayload to Task...")
        pull_request_payload = GitHubPullRequestPayload.model_validate_json(payload)
        return Task(
            event_type=TaskType.PULL_REQUEST,
            source_type=SourceType.GITHUB,
            user_id=user_id,
            url=pull_request_payload.pull_request.url,
            title=pull_request_payload.pull_request.title,
            body=pull_request_payload.pull_request.body,
            created_at=pull_request_payload.pull_request.created_at,
            updated_at=pull_request_payload.pull_request.updated_at,
        )


@lru_cache(maxsize=1)
def get_github_issue_transformer() -> ITransformer:
    return GitHubIssueTransformer()


@lru_cache(maxsize=1)
def get_github_pull_request_transformer() -> ITransformer:
    return GitHubPullRequestTransformer()


DIssueTransformer = Annotated[ITransformer, Depends(get_github_issue_transformer)]
DPullRequestTransformer = Annotated[
    ITransformer, Depends(get_github_pull_request_transformer)
]

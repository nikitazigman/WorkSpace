from abc import ABC, abstractmethod
from src.schemas.tasks import Task, TaskType
from src.schemas.common import CommonSchema
from src.schemas.issues import GithubIssuePayload
from src.schemas.pull_request import GithubPullRequestPayload
from typing import TypeVar, Generic
from functools import lru_cache

PayloadType = TypeVar("PayloadType", bound=CommonSchema)


class ITransformer(ABC, Generic[PayloadType]):
    @abstractmethod
    def transform(self, payload: PayloadType) -> Task:
        ...


class GitHubIssueTransformer(ITransformer[GithubIssuePayload]):
    def transform(self, payload: GithubIssuePayload) -> Task:
        return Task(
            event_type=TaskType.ISSUE,
            url=payload.issue.url,
        )


class GitHubPullRequestTransformer(ITransformer[GithubPullRequestPayload]):
    def transform(self, payload: GithubPullRequestPayload) -> Task:
        return Task(
            event_type=TaskType.PULL_REQUEST,
            url="",
        )


@lru_cache(maxsize=1)
def get_github_issue_transformer() -> ITransformer[GithubIssuePayload]:
    return GitHubIssueTransformer()


@lru_cache(maxsize=1)
def get_github_pull_request_transformer() -> ITransformer[GithubPullRequestPayload]:
    return GitHubPullRequestTransformer()

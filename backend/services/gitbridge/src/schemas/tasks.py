from src.schemas.common import CommonSchema
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class TaskType(StrEnum):
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"


class SourceType(StrEnum):
    GITHUB = "github"


class Task(CommonSchema):
    event_type: TaskType
    source_type: SourceType
    user_id: UUID
    url: str
    title: str
    body: str
    created_at: datetime
    updated_at: datetime

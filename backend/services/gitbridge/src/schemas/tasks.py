from src.schemas.common import CommonSchema
from enum import StrEnum


class TaskType(StrEnum):
    ISSUE = "issue"
    PULL_REQUEST = "pull_request"


class Task(CommonSchema):
    event_type: TaskType
    url: str

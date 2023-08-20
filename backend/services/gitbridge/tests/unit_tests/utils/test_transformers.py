import pytest
from src.utils.transformers import ITransformer, get_github_issue_transformer
from src.schemas.tasks import TaskType, SourceType
from uuid import UUID
from pathlib import Path


@pytest.fixture
def issue_transformer():
    return get_github_issue_transformer()


@pytest.fixture
def pull_request_transformer():
    return get_github_issue_transformer()


@pytest.fixture
def issue_payload() -> bytes:
    current_file = Path(__file__).resolve()
    test_payload = current_file.parent.parent / "data/github_issue_payload.json"
    return test_payload.read_bytes()


def test_transform(
    issue_transformer: ITransformer,
    issue_payload: bytes,
):
    user_id = UUID("9e9e9e9e-9e9e-9e9e-9e9e-9e9e9e9e9e9e")
    task = issue_transformer.transform(issue_payload, user_id)

    assert task.event_type == TaskType.ISSUE
    assert task.source_type == SourceType.GITHUB
    assert task.user_id == user_id
    # see the file data/github_issue_payload.json
    assert task.url == "https://api.github.com/repos/nikitazigman/test_repo/issues/1"
    assert task.title == "test"
    assert task.body == "test"

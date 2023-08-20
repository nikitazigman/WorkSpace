from fastapi import APIRouter, Header, Request, Path
from src.schemas.responses import BaseResponse
from src.services.github import (
    DGitHubIssueWebhookService,
    DGitHubPullRequestWebhookService,
)
from typing import Annotated
from uuid import UUID
from src.utils.exceptions import VerificationException

router = APIRouter()

DUserId = Annotated[
    UUID,
    Path(
        title="WorkSpace Infrastructure User ID",
        description="The internal user id of the workspace infrastructure",
    ),
]


@router.post(
    path="/issue/{user_id:uuid}",
    response_model=BaseResponse,
    summary="Github issue webhook handler",
    description="bridge between github issue webhook and a rabbitmq git queue",
)
async def issue_handler(
    user_id: DUserId,
    request: Request,
    service: DGitHubIssueWebhookService,
) -> BaseResponse:
    if "x-hub-signature-256" not in request.headers:
        raise VerificationException(detail="x-hub-signature-256 header is missing!")

    return await service.handle_webhook_payload(
        signature=request.headers["x-hub-signature-256"],
        payload_bytes=await request.body(),
        user_id=user_id,
    )


@router.post(
    path="/pull_request",
    response_model=BaseResponse,
    summary="Github pull request webhook handler",
    description="bridge between github pull request webhook and a rabbitmq git queue",
)
async def pull_request_handler(
    user_id: DUserId,
    request: Request,
    service: DGitHubPullRequestWebhookService,
) -> BaseResponse:
    if "x-hub-signature-256" not in request.headers:
        raise VerificationException(detail="x-hub-signature-256 header is missing!")

    return await service.handle_webhook_payload(
        signature=request.headers["x-hub-signature-256"],
        payload_bytes=await request.body(),
        user_id=user_id,
    )

from fastapi import APIRouter, Depends
from src.schemas.responses import BaseResponse
from src.schemas.issues import GithubIssuePayload
from fastapi.requests import Request
from loguru import logger
from src.services.github import get_github_issue_webhook_service, IGitHubWebhookService
from typing import Annotated

router = APIRouter()


@router.post(
    path="/issue",
    response_model=BaseResponse,
    summary="Github issue webhook handler",
    description="bridge between github issue webhook and a rabbitmq git queue",
)
async def issue_handler(
    request: Request,
    payload: GithubIssuePayload,
    service: Annotated[
        IGitHubWebhookService[GithubIssuePayload],
        Depends(get_github_issue_webhook_service),
    ],
):
    return await service.handle_webhook_payload(secret_key="mock key", payload=payload)


@router.post(
    path="/pull_request",
    response_model=BaseResponse,
    summary="Github pull request webhook handler",
    description="bridge between github pull request webhook and a rabbitmq git queue",
)
async def pull_request_handler(request: Request):
    data = await request.json()
    headers = request.headers
    logger.info(headers)
    logger.info(data)
    return BaseResponse()

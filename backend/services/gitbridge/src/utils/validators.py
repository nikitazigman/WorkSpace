from abc import ABC, abstractmethod
from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from src.utils.exceptions import VerificationException
import hashlib
import hmac
from loguru import logger


class ISecretValidator(ABC):
    @abstractmethod
    async def verify_signature(
        self, payload_body: bytes, secret_token: str, signature_header: str
    ) -> None:
        """Verify that the payload was sent from GitHub by validating SHA256.

        Raise and return 403 if not authorized.

        Args:
            payload_body: original request body to verify (request.body())
            secret_token: GitHub app webhook token (WEBHOOK_SECRET)
            signature_header: header received from GitHub (x-hub-signature-256)
        """


class GithubValidator(ISecretValidator):
    async def verify_signature(
        self, payload_body: bytes, secret_token: str, signature_header: str
    ) -> None:
        logger.debug("Verifying signature ...")

        hash_object = hmac.new(
            secret_token.encode("utf-8"),
            msg=payload_body,
            digestmod=hashlib.sha256,
        )

        expected_signature = "sha256=" + hash_object.hexdigest()
        if not hmac.compare_digest(expected_signature, signature_header):
            raise VerificationException(detail="Request signatures didn't match!")


@lru_cache(maxsize=1)
def get_github_validator() -> ISecretValidator:
    return GithubValidator()


DValidator = Annotated[ISecretValidator, Depends(get_github_validator)]

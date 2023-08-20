import pytest
from src.utils.validators import ISecretValidator, get_github_validator
from src.utils.exceptions import VerificationException
import hmac
import hashlib


@pytest.fixture
def validator() -> ISecretValidator:
    return get_github_validator()


@pytest.mark.asyncio
async def test_verify_signature_valid(validator: ISecretValidator, mock_logger_debug):
    payload_body = b"test_payload"
    secret_token = "secret_token"
    expected_signature = hmac.new(
        secret_token.encode("utf-8"),
        msg=payload_body,
        digestmod=hashlib.sha256,
    ).hexdigest()
    signature_header = f"sha256={expected_signature}"

    await validator.verify_signature(payload_body, secret_token, signature_header)

    mock_logger_debug.assert_called_once_with(
        f"Verifying signature: {payload_body=}, {secret_token=}, {signature_header=}"
    )


@pytest.mark.asyncio
async def test_verify_signature_missing_header(validator: ISecretValidator):
    payload_body = b"example_payload"
    secret_token = "your_secret_token"
    signature_header = None

    with pytest.raises(VerificationException):
        await validator.verify_signature(payload_body, secret_token, signature_header)


@pytest.mark.asyncio
async def test_verify_signature_invalid_signature(validator: ISecretValidator):
    payload_body = b"example_payload"
    secret_token = "your_secret_token"
    expected_signature = hmac.new(
        secret_token.encode("utf-8"),
        msg=b"different_payload",
        digestmod=hashlib.sha256,
    ).hexdigest()
    signature_header = f"sha256={expected_signature}"

    with pytest.raises(VerificationException):
        await validator.verify_signature(payload_body, secret_token, signature_header)

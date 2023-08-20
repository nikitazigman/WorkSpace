from fastapi.exceptions import HTTPException


class VerificationException(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(status_code=403, detail=detail)

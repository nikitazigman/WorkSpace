from src.schemas.common import CommonSchema
from uuid import UUID


class User(CommonSchema):
    id: UUID
    secret_key: str

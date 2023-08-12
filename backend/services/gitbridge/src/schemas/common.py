from pydantic import BaseModel, ConfigDict


class CommonSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

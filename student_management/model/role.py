from pydantic import BaseModel
from typing import List

class Role(BaseModel):
    role_id: int
    role_name: str
    role_description: str | None

class Roles(BaseModel):
    __root__: List[Role]

from __future__ import annotations

from typing import List

from pydantic import BaseModel, validator
from datetime import datetime


class User(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    address: str | None
    relgion: str | None
    caste: str | None
    role_id: int | None
    dob: datetime

    # @validator("dob")
    # def ensure_date_range(cls, v):
    #     if not datetime(year=1950, month=1, day=1) <= v < datetime(year=2017, month=1, day=1):
    #         raise ValueError("Must be in range")
    #     return v

class Users(BaseModel):
    __root__: List[User]

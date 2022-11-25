from __future__ import annotations

from typing import List

from pydantic import BaseModel, validator
from datetime import datetime, date


# > This class inherits from the BaseModel class, which is a class that inherits from the Model class, which is a class
# that inherits from the ndb.Model class
class User(BaseModel):
    # Defining the schema of the data.
    id: int
    name: str
    age: int
    gender: str
    address: str | None
    religion: str | None
    caste: str | None
    role_id: int | None
    dob: date

    @validator("dob", pre=True)
    def parse_birthdate(cls, value):
        """
        It takes a string in the format "YYYY-MM-DD" and returns a date object

        :param cls: The class that the method is bound to
        :param value: The value to be parsed
        :return: The date in the format of YYYY-MM-DD
        """
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()


# > This class inherits from the BaseModel class, which is a class that inherits from the Model class, which is a class
# that inherits from the ndb.Model class
class Users(BaseModel):
    # Defining the root of the JSON object.
    __root__: List[User]

from pydantic import BaseModel
from typing import List

'''
    `Role` is a class that has three attributes, `role_id`, `role_name`, and `role_description`, 
    where `role_id` is an integer, `role_name` is a string, and `role_description`
     is either a string or `None` 
 '''


class Role(BaseModel):
    role_id: int
    role_name: str
    role_description: str | None


# `Roles` is a list of `Role`s
class Roles(BaseModel):
    __root__: List[Role]

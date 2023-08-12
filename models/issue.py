from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel

from models.user import User


class Status(Enum):
    in_progress = "inProgress"
    incomplete = "incomplete"
    completed = "completed"


class Issue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    status: Status = Field()
    reporter: User = Field( foreign_key="user.id")

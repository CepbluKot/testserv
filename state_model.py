import pydantic
from enum import Enum


class LaunchTaskData(pydantic.BaseModel):
    task_data: str


class JobState(Enum):
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    IN_PROGRESS = 'IN_PROGRESS'


class JobData(pydantic.BaseModel):
    state: JobState|None = None
    output: str = ''

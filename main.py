import uvicorn
from fastapi import FastAPI
from uuid import uuid4
import time
from tasks import do_smth
from config import redis_async
from state_model import JobData, LaunchTaskData


app = FastAPI()


@app.post("/launch_task")
async def launch_task(task_data: LaunchTaskData):
    task_id = str(uuid4())

    do_smth.send(task_id, task_data.json())

    return {"task_id": task_id}


@app.get("/get_task_data")
async def get_task_data(task_id: str) -> JobData:
    job_data = await redis_async.get(task_id)
    job_data = JobData.parse_raw(job_data)

    return job_data


if __name__ == '__main__':
    uvicorn.run(app)    

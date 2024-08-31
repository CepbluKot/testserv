import time
import dramatiq
from dramatiq.brokers.redis import RedisBroker
from config import redis_sync
from state_model import JobData, JobState, LaunchTaskData


redis_broker = RedisBroker(host="localhost", namespace="dram-1")
dramatiq.set_broker(redis_broker)


@dramatiq.actor
def do_smth(task_id: str, task_data: str):
    new_task_stats = JobData(state=JobState.IN_PROGRESS.value)
    redis_sync.set(task_id, new_task_stats.json())
    time.sleep(10)
    res = (f"task_result: {task_data} !!!")
    new_task_stats = JobData(state=JobState.SUCCESS.value, output=res)
    redis_sync.set(task_id, new_task_stats.json())

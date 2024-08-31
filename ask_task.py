import time
import random
import requests
import json

from state_model import LaunchTaskData, JobData, JobState


def job_process():
    data = LaunchTaskData(task_data=str(random.randint(1, 100)))
    res= requests.post(f'http://localhost:8000/launch_task', data=data.json())
    resp = json.loads(res.text)

    task_id = (resp['task_id'])
    
    work_res_parsed = JobData()
    while work_res_parsed.state != JobState.SUCCESS and work_res_parsed.state != JobState.FAIL: 
        work_res= requests.get(f'http://localhost:8000/get_task_data?task_id={task_id}')
        while not work_res:
            work_res= requests.get(f'http://localhost:8000/get_task_data?task_id={task_id}')
            
        work_res_parsed = JobData.parse_raw(work_res.text)

        # print(work_res_parsed)
        # print('wip', work_res_parsed.state != JobState.SUCCESS , work_res_parsed.state != JobState.FAIL)
        # print('wip')
        time.sleep(1)


    print('sucess', work_res_parsed)


import threading

for _ in range(5):
    t1 = threading.Thread(target=job_process)
    t1.daemon=True
    t1.start()

time.sleep(20)

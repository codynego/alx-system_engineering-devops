#!/usr/bin/python3

# a Python script that, using this REST API, for a given employee ID,
# returns information about his/her TODO list progress

import requests
import json
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)
    response = requests.get(user_url)
    dict_response = json.loads(response.text)
    name = dict_response[0].get('name')
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    task_response = requests.get(tasks_url)
    task_data = json.loads(task_response.text)
    total = len(task_data)
    completed = 0
    completed_task = []
    for task in task_data:
        if task.get('completed'):
            completed += 1
            completed_task.append(task)

    print(f"Employee {name} is done with task({completed}/{total}):")

    for task in completed_task:
        print("\t {}".format(task.get('title')))

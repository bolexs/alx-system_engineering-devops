#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    """Information gathering from an API"""
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos?userId={}".format(user_id)).json()
    completed_tasks = []

    for task in todo:
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todo)))
    for task in completed_tasks:
        print("\t {}".format(task))

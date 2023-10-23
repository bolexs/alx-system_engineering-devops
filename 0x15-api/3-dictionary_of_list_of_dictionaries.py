#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Getting data from an api and exporting to JSON"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()
    tasks = {}
    for user in users:
        user_id = user.get("id")
        tasks[user_id] = []
        for task in todo:
            if user_id == task.get("userId"):
                tasks[user_id].append({"task": task.get("title"),
                                       "completed": task.get("completed"),
                                       "username": user.get("username")})
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(tasks, jsonfile)

#!/usr/bin/python3
"""Gather data from an API and export to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    """Information gathering from an API and convert to csv"""
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos?userId={}".format(user_id)).json()
    with open("{}.csv".format(user_id), "w") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([user_id, user.get("username"),
                            task.get("completed"), task.get("title")])

#!/usr/bin/python3
"""Gather all data from an API"""
import requests


def top_ten(subreddit):
    """ Queries the Reddit API and returns the title of the first 10 posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    param = {'limit': 10}


    response = requests.get(url, headers=headers, param=param, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for kid in children:
            upload = kid.get('data', {})
            title = upload.get('title', '')
            print(title)
    else:
        print('None')

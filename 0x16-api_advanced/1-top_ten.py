#!/usr/bin/python3
"""Gather data from an API"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            post = child.get('data', {})
            title = post.get('title', '')
            print(title)
    else:
        print(None)
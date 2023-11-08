#!/usr/bin/python3
"""Gather data from an API"""
import requests



def recurse(subreddit, hot_list=[], after=None):
    """ Queries the Reddit API and returns a list of all the hot articles for a given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My user Agent 1.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for kid in children:
            post = kid.get('data', {})
            title = post.get('title', '')
            hot_list.append(title)
        after = data.get('after', None)
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

#!/usr/bin/python3
"""
Module has function top_ten
"""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(base_url, allow_redirects=False)

    if response.status_code == 200:
        hot_posts = response.json()["data"]["children"]
        for i in range(0, 9):
            try:
                print(hot_posts[i]["data"]["title"])
            except Exception as e:
                return
    return
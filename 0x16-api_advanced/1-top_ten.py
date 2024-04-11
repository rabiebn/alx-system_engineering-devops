#!/usr/bin/python3
"""
Module has function top_ten
"""
import requests
from time import sleep


def top_ten(subreddit):
    """Print titles of the first 10 hot posts"""
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    while True:
        response = requests.get(base_url, allow_redirects=False)
        if response.status_code == 200:
            break
        elif response.status_code == 429:
            sleep(5)
            continue
        else:
            break

    try:
        hot_posts = response.json()["data"]["children"]
        for i in range(10):
            print(hot_posts[i]["data"]["title"])
    except Exception as e:
        print("None")

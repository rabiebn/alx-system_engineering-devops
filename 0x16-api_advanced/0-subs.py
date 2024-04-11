#!/usr/bin/python3
"""Module has function number_of_subscribers"""
import requests
from time import sleep


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    while True:
        response = requests.get(base_url, allow_redirects=False)
        if response.status_code == 200:
            break
        elif response.status_code == 429:
            sleep(5)
            continue
        else:
            return 0
    try:
        return response.json()["data"]["subscribers"]
    except Exception as e:
        return 0

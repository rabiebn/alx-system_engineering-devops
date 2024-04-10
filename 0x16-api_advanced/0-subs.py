#!/usr/bin/python3
"""Module has function number_of_subscribers"""
import requests
from time import sleep


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "Python-requests",
        "Content-Type": "aplication/json"
        }
    response = requests.get(base_url,
                            headers=header,
                            allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]

    return 0

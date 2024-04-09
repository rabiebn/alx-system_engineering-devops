#!/usr/bin/python3
"""Module has function number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    base_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(base_url,
                            headers={"User-Agent": "whiteJhendrix"},
                            allow_redirects=False)

    if response.status_code == 200:
        return response.json()["data"]["subscribers"]

    return 0

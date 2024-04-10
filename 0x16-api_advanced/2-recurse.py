#!/usr/bin/python3
"""
Module has function recurse
"""
import requests
from time import sleep


def recurse(subreddit, hot_list=[], after=""):
    """Lists titles of all of hot posts"""
    base_url = "https://www.reddit.com/r/"
    header = {"User-Agent": "mir"}

    while True:
        try:
            response = requests.get("{}{}/hot.json?after={}".format(base_url,
                                                                    subreddit,
                                                                    after),
                                    headers=header,
                                    allow_redirects=False)
            break
        except requests.exceptions.ConnectionError as e:
            sleep(5)
            continue

    if response.status_code == 200:
        data = response.json()["data"]
        for post in data["children"]:
            hot_list.append(post["data"]["title"])

        if data["after"] is not None:
            recurse(subreddit, hot_list, after=data["after"])

        return hot_list

    return None

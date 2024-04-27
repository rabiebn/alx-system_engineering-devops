#!/usr/bin/python3
"""Module has function number_of_subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    return 0

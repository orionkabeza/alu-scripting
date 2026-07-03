#!/usr/bin/python3
"""
Module that queries the Reddit API for a subreddit's subscriber count.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a
    given subreddit.

    Args:
        subreddit (str): the name of the subreddit to search.

    Returns:
        int: the number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api_advanced:v1.0 (by /u/bot)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0

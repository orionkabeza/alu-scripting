#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""
import requests
import time


def top_ten(subreddit):
    """
    Query the Reddit API and print the titles of the first 10 hot
    posts listed for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit to search.

    Prints:
        The titles of the first 10 hot posts, one per line, or
        None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:api_advanced.alu_scripting:v1.0 (by /u/alu)"
    }
    params = {"limit": 10}

    response = None
    for attempt in range(3):
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code in (429, 403, 500, 502, 503):
            time.sleep(1 + attempt)
            continue
        break

    if response is None or response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    if not posts:
        print(None)
        return

    for post in posts:
        print(post.get("data", {}).get("title"))

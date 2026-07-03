#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""
import requests


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
    headers = {"User-Agent": "linux:0x16.api_advanced:v1.0 (by /u/bot)"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
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

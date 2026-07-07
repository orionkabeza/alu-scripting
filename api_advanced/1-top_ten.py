#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.
    If subreddit is invalid, prints None.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        "User-Agent": "ALU-Script/1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Output check: invalid subreddit or blocked request
        if response.status_code != 200:
            print(None)
            return

        data = response.json()

        posts = data.get("data", {}).get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

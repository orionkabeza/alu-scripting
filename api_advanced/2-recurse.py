#!/usr/bin/python3
"""
Module that recursively queries the Reddit API and returns a list of
all hot article titles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): the name of the subreddit to search.
        hot_list (list): the accumulated list of titles (used
            internally for recursion, do not supply manually).
        after (str): the pagination token for the next page (used
            internally for recursion, do not supply manually).

    Returns:
        list: titles of all hot articles, or None if the subreddit
            is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api_advanced:v1.0 (by /u/bot)"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    posts = data.get("children", [])
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)

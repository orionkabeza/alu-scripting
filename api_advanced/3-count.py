#!/usr/bin/python3
"""
Module that recursively queries the Reddit API, parses the titles of
all hot articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively query the Reddit API and print a sorted count of
    given keywords found in the titles of hot articles.

    Args:
        subreddit (str): the name of the subreddit to search.
        word_list (list): the list of keywords to count.
        after (str): the pagination token for the next page (used
            internally for recursion, do not supply manually).
        counts (dict): the accumulated word counts (used internally
            for recursion, do not supply manually).

    Prints:
        The keyword counts sorted in descending order by count, then
        ascending alphabetically, one per line as "keyword: count".
        Prints nothing if the subreddit is invalid or no matches
        are found.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            key = word.lower()
            counts.setdefault(key, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api_advanced:v1.0 (by /u/bot)"}
    params = {"limit": 100, "after": after}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
    except ValueError:
        return

    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "")
        for token in title.lower().split():
            if token in counts:
                counts[token] += 1

    after = data.get("after")
    if after is not None:
        count_words(subreddit, word_list, after, counts)
        return

    sorted_counts = sorted(
        counts.items(), key=lambda item: (-item[1], item[0])
    )
    for word, count in sorted_counts:
        if count > 0:
            print("{}: {}".format(word, count))

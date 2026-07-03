# api_advanced

Advanced scripting with the Reddit API.

## Description

This project uses Python 3 and the `requests` module to interact with
the Reddit API. It covers reading paginated API results, making
recursive API calls, parsing JSON responses, and sorting the parsed
data.

## Requirements

- Python 3.4.3 on Ubuntu 14.04 LTS
- `requests` module
- All files start with `#!/usr/bin/python3`, end with a newline, are
  executable, and follow PEP 8 style.
- No authentication is required; a custom `User-Agent` header is used
  and redirects are disabled so invalid subreddits are detected
  correctly instead of following Reddit's search redirect.

## Files

| File | Description |
| --- | --- |
| `0-subs.py` | `number_of_subscribers(subreddit)` — returns the subscriber count for a subreddit, or 0 if invalid. |
| `1-top_ten.py` | `top_ten(subreddit)` — prints the titles of the first 10 hot posts, or `None` if invalid. |
| `2-recurse.py` | `recurse(subreddit, hot_list=[])` — recursively returns a list of all hot post titles using pagination, or `None` if invalid. |
| `3-count.py` | `count_words(subreddit, word_list)` — recursively counts keyword occurrences across all hot post titles and prints them sorted by count (desc) then alphabetically (asc). |

## Usage

```
./0-main.py <subreddit>
./1-main.py <subreddit>
./2-main.py <subreddit>
./3-main.py <subreddit> '<word1> <word2> ...'
```

#!/usr/bin/python3
"""Top ten posts"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    res = requests.get(url, headers=headers)

    if res.status != 200:
        print(none)
    else:
        data = res.json().get('data').get('children')
        for post in data:
            print(post.get('data').get('title'))

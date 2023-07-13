#!/usr/bin/python3
""" function that queries the Reddit API and \
    returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return 0
    else:
        return res.json().get('data').get('subscribers')

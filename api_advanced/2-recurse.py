#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a \
    list containing the titles of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My Agent 1.0'}
    param = {'after': after}
    res = requests.get(url, headers=headers, params=param)

    if res.status_code != 200:
        return None
    else:
        json_res = res.json()
        after = json_res.get('data').get('after')
        has_next = json_res.get('data').get('after') is None
        hot_articles = json_res.get('data').get('children')
        [hot_list.append(article.get('data').get('title'))
         for article in hot_articles]

        return recurse(subreddit, hot_list, after=after) \
            if has_next else hot_list

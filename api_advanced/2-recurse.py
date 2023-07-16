#!/usr/bin/python3
"""recursive function that queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My Agent 1.0'}
    params = {'after': after}
    res = requests.get(url, headers=headers, params=params)
    
    if res.status != 200:
	return None

    else:
        json_res = res.json()
        after = json_res.get('data').get('after')
        has_next = json_res.get('data').get('data') is not None
        
        hot_articles = json_res.get('data').get('children')
        [hot_list.append(article.get('data').get('title'))
         for article in hot_articles]
        
        return recurse(subreddit, hot_list, after=after) if has_next \
            else hot_list

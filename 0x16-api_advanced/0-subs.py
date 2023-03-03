#!/usr/bin/python3

import requests

""" Function that uses Reddit Api """


def number_of_subscribers(subreddit):
    """ Returns the number of subscriber for a given subreddit """

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

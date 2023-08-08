#!/usr/bin/python3
"""
Queries the Reddit API to get the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for the given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot'}  # Set a custom User-Agent
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0

if __name__ == "__main__":
    subreddit_name = input("Enter a subreddit name: ")
    num_subscribers = number_of_subscribers(subreddit_name)
    print(f"{subreddit_name} has {num_subscribers} subscribers.")

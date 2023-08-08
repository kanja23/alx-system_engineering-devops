#!/usr/bin/python3
"""
Queries the Reddit API to print the titles of the first 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for the given subreddit.
    If the subreddit is invalid, prints None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot'}  # Set a custom User-Agent
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        if not posts:
            print("No posts found.")
            return
        
        print(f"Top 10 hot posts in /r/{subreddit}:\n")
        for i, post in enumerate(posts[:10], start=1):
            title = post['data']['title']
            print(f"{i}. {title}")
    else:
        print("None")

if __name__ == "__main__":
    subreddit_name = input("Enter a subreddit name: ")
    top_ten(subreddit_name)

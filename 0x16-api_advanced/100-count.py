#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests

def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'MyBot/1.0'}  # Set a user agent to identify your bot

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Invalid subreddit or error in retrieving data.")
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word in title and is_whole_word(title, word):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    after = data['data']['after']

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            print(f'{word}: {count}')

def is_whole_word(text, word):
    return f' {word} ' in f' {text} '

# Example usage
subreddit_name = 'python'
keywords = ['python', 'programming', 'tutorial', 'code']
count_words(subreddit_name, keywords)

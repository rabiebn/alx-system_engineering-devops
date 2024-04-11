#!/usr/bin/python3
"""Module has count_words"""
import requests
recurse = __import__("2-recurse").recurse


def count_words(subreddit, word_list):
    """
    Prints sorted count of given keywords in a list of hot articles' titles
    """
    hotList = recurse(subreddit)

    word_dict = dict()
    for i in range(len(word_list)):
        for j in range(len(word_list)):
            if i == j:
                continue
            else:
                if word_list[j].casefold() == word_list[i].casefold():
                    word_list.pop(j)
        word_dict[word_list[i]] = 0

    for word in word_list:
        for article in hotList:
            if word.casefold() in article.casefold():
                word_dict[word] += 1

    word_dict = {k: v for k, v in sorted(word_dict.items(),
                                         key=lambda item: item[1],
                                         reverse=True)}
    for key, val in word_dict.items():
        if val > 0:
            print("{}: {}".format(key, val))

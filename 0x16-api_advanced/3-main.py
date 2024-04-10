#!/usr/bin/python3
"""
Module has count_words
"""
import requests
recurse = __import__('2-recurse').recurse


def count_words(subreddit, word_list):
    """Counts number of accurence of each word from word_list"""
    

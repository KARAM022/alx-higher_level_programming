#!/usr/bin/python3
"""Fetches url from command line argument"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    """check the type of response"""
    print(response.headers.get('X-Request-Id'))

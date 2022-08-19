#!/usr/bin/python3
"""Task 1. Response header value #0"""
from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    print(response.headers.get('X-Request-Id'))

#!/usr/bin/python3
"""Task 0. What's my status? #0"""
from urllib.request import urlopen

with urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print('Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
      .format(type(html), html, html.decode('utf-8')))

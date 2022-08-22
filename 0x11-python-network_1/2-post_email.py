#!/usr/bin/python3
"""Task POST an email #0"""
if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1] 
    params = {"mail": argv[2]}    
 
    query_string = urlencode( params ) 
 
    url = url + "?" + query_string 
 
    with urlopen( url ) as response: 
        response_text = response.read() 
        print( response_text ) 
#!/usr/bin/python

import requests

target_urls = input("Input full path to the text file\n")

url_list = []

def read_from_file(filename):
    '''Read urls from the file and store them in a list'''
    source_list = [] # Temporary list inside the function
    with open(filename, "r") as file:
        for line in file:
            source_list.append(line.rstrip())
    return source_list # Return the full list

def probe(url):
    '''Main probe function that checks status codes and prints results'''

    try:
        response = requests.get(url, timeout=5, allow_redirects=False)

        if response.status_code == 200:
            print(f"{url} - {response.status_code} - Resolved")
        elif response.status_code == 301 or response.status_code == 302:
            print(f"{url} - {response.status_code} - is redirected to - {str(response.headers['Location'])}")
        elif response.status_code == 404:
            pass
        elif response.status_code == 403:
            print(f"{url} - {response.status_code} - Forbidden")
        elif response.status_code == 401:
            print(f"{url} - {response.status_code} - Unauthorized")

    except OSError:
        print(url + " - Not resolving")

    except ConnectionError:
        print(url + " - Connection Error")
    
    except TimeoutError:
        print(url + " - Timed Out")



url_list = read_from_file(target_urls) # Stores the returned list in a global scope
for url in url_list:
    probe(url)

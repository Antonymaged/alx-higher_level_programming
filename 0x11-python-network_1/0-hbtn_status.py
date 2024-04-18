#!/usr/bin/python3
import urllib.request

def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", utf8_content)

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_status(url)

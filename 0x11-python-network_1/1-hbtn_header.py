#!/usr/bin/python3
import urllib.request
import sys
if(__name__=="__main__"):
    sys.exit(0)
else:
    f = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(f) as h:
        print(h.getheader('X-request-id'))

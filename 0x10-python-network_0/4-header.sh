#!/bin/bash
#lunch a get request to the url the user enters and ading a header
curl -sX GET "$1" HTTP/1.1 -H "X-School-User-Id:98" 

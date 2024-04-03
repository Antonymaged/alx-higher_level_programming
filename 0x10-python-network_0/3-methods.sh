#!/bin/bash
#knowing what is the requests the url can make
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

#!/bin/bash
#lunch a delete request to the url the user enter
curl -sX DELETE "$1" HTTP/1.1

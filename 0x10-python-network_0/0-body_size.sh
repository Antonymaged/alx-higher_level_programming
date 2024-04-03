#!/bin/bash
#desplaing the body size of the url the user enters
curl -s -w"%{size_download}\n" -o /dev/null $1

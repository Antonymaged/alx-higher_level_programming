#!/bin/bash
#lunch a post request wit the default data
curl -sX POST "$1" HTTP/1.1 -d "email=test@gmail.com&subject=I will always be here for PLD"

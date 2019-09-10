#!/bin/bash

# Paste post page curl command here and pipe it to response.txt

python parser.py

while read name
do
    # Paste poke command here. Replace the target ID with $name make sure it
    # is using double quotes. You can pipe this to the poke_output.txt
    # and it will be ignored
    sleep 1 #  TODO make random
done < targets.txt

#!/bin/bash

score=0
python3 main.py  < input.txt > output.txt 2>&1

if [ $? -eq 0 ]; then
    ((score=score+1))
else
	echo "We finished with and error!"
    exit 0
fi

echo $score

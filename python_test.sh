#!/usr/bin/expect

python3 hello_world.py < input.txt &> output.txt

echo $?

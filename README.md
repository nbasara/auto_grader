<h1 align="center">Auto Grader</h1>

### Necessary Files

In .zip
* ArrayList.py 
* ArrayQueue.py 
* BookStore.py

input.txt OutputGrader.py python_test.sh

## Requirements

Unix file system with the unzip command and ability to run bash scripts.

## How to Use

Create a grading environment with all template files excluding the necessary files from student's
assignment.  
Have the students submit a zip file containing the necessary files to dropbox via beachboard. Be sure the files are zipped and not a folder.
The bash script assumes there is no underlying directory in the zip.

In the grading environment include input.txt, OutputGrader.py, python_test.sh, and all of the files from dropbox.

I have ran and devloped on ubuntu linux. Although you will also be able to run on WindowsSubsystemLinux or GITBash.

To run on Linux
`chmod +x python_test.sh`

`bash python_test.sh > asgn1Grades.txt`


## Description

Auto grader script that will automatically give input to a python program and be able to comapare the output. After that be able to give an appropriate grade based on the the difference from the expected output. Be able to run for a class at a time.

### To Do 

- [x] Given a python file be able to give user input from input file
- [x] Output of python file to output.txt
- [x] Be able to detect when a program crashes
- [x] Give clean output for various benchmarks
- [x] Write output from grade to student folders
- [x] Write a script that will grade the students output
- [x] Write single file detailing student names and student grades

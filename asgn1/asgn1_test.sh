#!/bin/bash

for s in *.zip; do
    # copy the necessary files into working directory
    #students score for demo
    score=0
    #parse to get student name
    readarray -d '- ' -t stdArr <<< "$s"
    studentName="${stdArr[2]}"
    studentName="$(echo -e "${studentName}" | tr -d '[:space:]')"
    unzip -qq "$s" -d $studentName
    student=${s::-4}
    cp "$studentName"/ArrayList.py .
    cp "$studentName"/ArrayQueue.py .
    cp "$studentName"/BookStore.py .
    #run program on input from input.txt, with output + errors being
    #written to output.txt
    python3 main.py  < input.txt > output.txt 2>&1 
    #check if last command exited with error in program
    if [ $? -eq 0 ]; then
        ((score=score+1))
        #run the autograder for the students output
        python3 OutputGrader.py 
        if [ $? -eq 0 ]; then
            ((score=score+1))
        fi
        mv reason.txt "$studentName"
        echo "${studentName} ${score}"
    else
        # change this to output the student name and their grade of  0
        echo "${studentName} 0"
        #move their error to student directory for saving for later
        mv output.txt "$studentName"/reason.txt
    fi

    #change this to be student name and grade

    # rm student files to do again
    rm ArrayList.py 
    rm ArrayQueue.py 
    rm BookStore.py 
done

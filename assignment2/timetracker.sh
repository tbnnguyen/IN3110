#!/bin/bash

label=""
time1=""

function track_start {
    LOGFILE=logfile.txt
    if ! test -f "$LOGFILE"; then
        touch logfile.txt
    fi

    time1=$(date +"%T")
    
    if [ -z $label ]; then
        label=$1
        #Check if there is a label
        if [ -z $label ]; then
            echo You need to create a label
        else 
            echo -e "START $(date) \nLABEL This is task $label" >> $LOGFILE
        fi
    else 
        echo There is already a task running
    fi
}

function track_stop {
    time2=$(date +"%T")

    if [ -z $label ]; then
        echo No current task running
    else 
        echo -e "END $(date) \n" >> $LOGFILE
    fi

    #Resetting label and start time
    label=""
    time1=""
}

function track_status {
    if [ -z $label ]; then
        echo No current task running
    else 
        echo $label is currently running
    fi
}

function track_log {
    input="$LOGFILE"
    labelName=""
    startTime=""
    endTime=""
    paragraphHead=0

    #NB! Will not do task names with spaces
    while IFS= read -r line; do
        let "paragraphHead++"
        wordcount=0
        for word in $line; do
            let "wordcount++"
            if [ "$paragraphHead" -eq "1" ] && [ "$wordcount" -eq "5" ]; then
                startTime=$word
            fi
            if [ "$paragraphHead" -eq "2" ] && [ "$wordcount" -ge "5" ]; then
                labelName="$word"
            fi
            if [ "$paragraphHead" -eq "3" ] && [ "$wordcount" -eq "5" ]; then
                endTime=$word
                startTime=$(echo $startTime | sed 's/^/((/; s/:/)*60+/g' | bc)
                endTime=$(echo $endTime | sed 's/^/((/; s/:/)*60+/g' | bc)
    
                elapsedSec=$(($endTime-$startTime))

                #Converting to HH:MM:SS
                elapsedTime=$(printf '%02dh:%02dm:%02ds\n' $(($elapsedSec/3600)) $(($elapsedSec%3600/60)) $(($elapsedSec%60)))
                echo $labelName": "$elapsedTime 
                labelName=""
                paragraphHead=-1
            fi
        done
    done < "$input"
}




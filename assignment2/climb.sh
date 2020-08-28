#!/bin/bash

function climb {
    # default er 1 mappe opp om man ikke oppgir parameter
    num=1
    if [ $# -gt 0 ]; then
        num=$1
    fi
    # navigerer antall mapper basert på variabel "num"
    while [ $num -ne 0 ]; do
        cd ..
        num=$((num-1))
    done
    
}

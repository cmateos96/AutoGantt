#!/bin/bash

CODE_PATH=$(realpath $0)
CODE_PATH=${CODE_PATH/"AutoGantt.sh"/}
PROGRAM_FILES_PATH=${CODE_PATH/"Code/"/}"Program_Files"

python3 ${CODE_PATH}AutoGantt.py
if [ $? -eq 0 ]
    then
        TJP_FILE=$(find $PROGRAM_FILES_PATH -name "*.tjp")
        if ! [ -d Gantt_Results ]
            then
                mkdir Gantt_Results
        fi
        cd Gantt_Results
        echo "Comienza TaskJuggler:"
        tj3 $TJP_FILE
        if [ $? = 0 ]
            then
            if [ -f Diagrama\ de\ Gantt\ *.html ]
                then
                    python3 -mwebbrowser Diagrama\ de\ Gantt\ *.html
            fi
        fi
        cd -
fi
#!/bin/bash

"$@" &
myPid=$!
OUT=./$myPid.metrics.csv
echo "TS;MEM;CPU;DISK" > $OUT
while kill -0 "$myPid"
do
    TS=$(date +%s)
    MEM=$(free | grep Mem | tr -s ' ' |  cut -d' ' -f3)
    CPU=$(ps -A -o pcpu | tail -n+2 | paste -sd+ | bc)
    # DISK=$(df . | tail -1 | cut -d' ' -f3)
    DISK=$(df /data | tail -1 | cut -d' ' -f3)
    echo "$TS;$MEM;$CPU;$DISK" >> $OUT
    sleep 1
done
echo "OUT=$OUT"

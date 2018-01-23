#!/bin/bash
PS=
Endpoint=`/bin/grep hostname /data1/falcon-agent/cfg.json|awk -F "\"" '{print $4}'`
Time=`date +%Y-%m-%d `
DIR="/data1/minisearch/msearch/"
CMD=`cd $DIR && ./idx_stat |grep disk_index`
total=`cd $DIR && ./idx_stat|awk -F ":" '/^total/ {print $2}'`
disk_index=`echo $CMD|awk '{print $1}'|cut -d [ -f 2|cut -c 1`
time_index=`echo $CMD|awk '{print $6}'|cut -d : -f 2`
echo $time_index
if [ $disk_index -eq 3 ] || [ $disk_index -eq 4 ] && [ $Time = $time_index ]
then
	disk_index=1
else
	disk_index=0
fi
ts=`date +%s`
curl -X POST -d "[{\"metric\": \"h0_index\", \"endpoint\": \"$Endpoint\", \"timestamp\": $ts,\"step\": 3600,\"value\": $total,\"counterType\": \"GAUGE\",\"tags\": \"h0_index=total_index\"}]" http://127.0.0.1:1988/v1/push

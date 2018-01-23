#!/bin/env python
#-*- coding:utf-8 -*-


import os,sys
import time
import json
import commands

#定义监控端口
port=[11311,11611]

#获取监控地址
with open('/data1/falcon-agent/cfg.json','r') as f:
    json_file=json.loads(f.read())
    endpoint=json_file['hostname']
hostip=endpoint.split('"')[0]

#定义监控项
########监控使用内存大小
data = []
for ip_port in port: 
	cmd ="echo stats | nc %s %s|grep -w 'STAT bytes'|awk '{print(int($3))}'"   % (hostip,ip_port)
	result= commands.getoutput(cmd)
        t = {}
        t['endpoint'] = hostip
        t['timestamp'] = int(time.time())
        t['step'] = 60
        t['counterType'] = 'GAUGE'
        t['metric'] = 'memchached.mem.used'
        t['value']= result
        t['tags'] = 'port=%s' % ip_port

        data.append(t)
print json.dumps(data)


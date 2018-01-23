#!/bin/env python
#-*- coding:utf-8 -*-
####敏感词插件
import os,sys
import os.path
import socket
import time
import json
import copy
import urllib2

data=[]
hostip = socket.gethostname()
try:
	output=urllib2.urlopen("http://%s/search/intra.php?cuid=12345678&q=法轮功&sid=ping&xsort=social&us=1" % hostip).read()
	out = json.loads(output)[3]
except urllib2.HTTPError,e:
	print e.code
	sys.exit()
t = {}
t['metric'] = "keywords_page_check"
t['endpoint'] = hostip
t['timestamp'] = int(time.time())
t['step'] = 60
t['counterType'] = 'GAUGE'
t['tags'] = 'error_code=21401'
t['value'] = out['error_code']
data.append(t)
 
if data:
    print json.dumps(data)
      
      



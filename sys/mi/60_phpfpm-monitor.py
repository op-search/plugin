#!/bin/env python
#-*- coding:utf-8 -*-

import os,sys
import os.path
from os.path import isfile
from traceback import format_exc
import xmlrpclib
import socket
import time
import json
import copy
import commands
import urllib2

data=[]
i=1
hostip = socket.gethostname()
try:
	output=urllib2.urlopen("http://%s/phpfpm_status?json" % hostip).read()
	out=json.loads(output)
except urllib2.HTTPError,e:
	print e.code
	sys.exit()

for key in out.keys():
      	t = {}
	key_d ='.'.join(key.split())
	if ( key_d == 'start.time' or key_d == 'start.since' or key_d == 'pool' ):
		  continue 
      	t['metric'] =  '.'.join(key.split())
      	t['endpoint'] = hostip
      	t['timestamp'] = int(time.time())
      	t['step'] = 60
      	t['counterType'] = 'GAUGE'
      	t['tags'] = 'name=phpfpm'
      	t['value'] = out[key]
      	i+=1  
      	data.append(t)
 
if data:
    print json.dumps(data)

      
      



#!/usr/bin/env python
from sh import node, curl
from functools import partial
import time
import simplejson as json

'''
------------------------------ Script artifacts ----------------------------
'''

def log(msg, *params): 
    print(msg.format(*params) if (params) else msg)

def logFromClient(*params):
    client = params[0]
    msgLine = params[1]
    if ("data:" in msgLine):
        log("Client {} received: {}", client, msgLine)

def send(data, path):
    msg = json.dumps(data)
    log("Sending: \'{}\' to {}\n", msg, path)
    curl("-i", "-H", 'Content-Type: application/json', "-d", msg, "127.0.0.1:9001/%s" % path)

'''
------------------------------ Script -------------------------------------
'''
sseClient = './client.js'

send({'label': 'Akka'}, 'flows')

for i in range(1, 5):
    node(sseClient, _bg = True, _out = partial(logFromClient, i))
    time.sleep(1)
    send({'text': "message%s" % i}, "flows/akka/messages")


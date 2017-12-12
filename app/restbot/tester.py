#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from os.path import dirname,realpath
sys.path.append(dirname(dirname(realpath(__file__))))

import app.restbot.asserter
import requests
from requests.exceptions import ConnectionError

def doTest(url,test,expected,global_headers,verifySsl=True):
    full_url = url + test['path']
    headers = test.get('headers',{})
    for name in global_headers.keys():
        headers[name] = global_headers[name]

    data = test.get('data',{})
    try:
        request = test['request']
        response = doRequest(full_url,request,headers,data,verifySsl)
    except requests.exceptions.ConnectionError:
        return False,'[ConnectionError]'

    return app.restbot.asserter.assert_response(response,expected)

def doRequest(url,request,headers={},data={},verify=True):
    request = request.lower()
    if request == 'get':
        response = requests.get(url,headers=headers,verify=verify)
    elif request == 'post':
        response = requests.post(url,json=data,headers=headers,verify=verify)
    elif request == 'put':
        response = requests.put(url,json=data,headers=headers,verify=verify)
    elif request == 'delete':
        response = requests.delete(url,headers=headers,verify=verify)
    else:
        raise Exception("Unsupported HTTP method: %s" % request)

    return response

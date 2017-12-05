#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from os.path import dirname,realpath
sys.path.append(dirname(dirname(realpath(__file__))))

import apie.asserter
import requests
from requests.exceptions import ConnectionError

def doTest(url,test,expected,global_headers):
    full_url = url + test['path']
    headers = test.get('headers',{})
    for header_data in global_headers:
        name = header_data['name']
        value = header_data['value']
        headers[name] = value

    data = test.get('data',{})
    try:
        request = test['request']
        response = doRequest(full_url,request,headers,data)
    except requests.exceptions.ConnectionError:
        return False,'[ConnectionError]'

    return apie.asserter.assert_response(response,expected)

def doRequest(url,request,headers={},data={}):
    request = request.lower()
    if request == 'get':
        response = requests.get(url,headers=headers)
    elif request == 'post':
        response = requests.post(url,data=data,headers=headers)
    elif request == 'put':
        response = requests.put(url,data=data,headers=headers)
    elif request == 'delete':
        response = requests.delete(url,headers=headers)
    else:
        raise Exception("Unsupported HTTP method: %s" % request)

    return response

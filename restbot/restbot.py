#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
from os.path import abspath,dirname,realpath
import app.restbot.parser
import app.restbot.header_parser
import app.restbot.asserter
import app.restbot.tester
import time

def main_multiple(args):
    testsuite_file = abspath(args.get("test_script"))
    testsuite_dir = abspath(dirname(testsuite_file))
    print("testsuite_dir",testsuite_dir)
    testsuite = app.restbot.parser.testsuite_fromfile(testsuite_file)
    for testsuite_item in testsuite:
        name = testsuite_item["name"]
        test_script = testsuite_dir + os.sep + testsuite_item["file"]
        args["test_script"] = test_script
        print("============================")
        print(name)
        print("============================")
        main(args)

def main(args):
    global_headers = {}
    if args.get('headers_script') is not None:
        global_headers = app.restbot.header_parser.parseFile(args['headers_script'])

    global_headers['Content-Type'] = 'application/json'

    testdata = app.restbot.parser.parseFile(args['test_script'])
    url = testdata['url']
    showOnlyErrors = args.get('errors')
    verifySsl = args.get('insecure') is False
    if verifySsl is False:
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        print("InsecureRequestWarning: Unverified HTTPS request are going to be made")
        time.sleep(3)

    test_total = 0
    error_total = 0
    time_begin = time.time()
    for item in testdata['tests']:
        test = item['test']
        expected = item['expected']
        test_result, data = app.restbot.tester.doTest(url,test,expected,global_headers,verifySsl)

        if not test_result:
            error_total += 1
            exp_type = list(expected.keys())[0]
            actual_type = 'actual_%s' % exp_type.replace('expected_','')
            expected[actual_type] = data

        if test_result:
            if not showOnlyErrors:
                print("Test: %s" % test['name'])
                print("Result: OK")
                print("") #newline
        else:
            print("Test: %s" % test['name'])
            print("Result: ERROR")
            print(expected)
            print("") #newline

        test_total += 1
        # Support sleep field
        if test.get('sleep'):
            iseconds = int(test.get('sleep'))
            print("~~~ sleeping for %d seconds" % iseconds)
            time.sleep(iseconds)

    time_total = int(round((time.time()-time_begin) * 1000))

    print("Time: %d ms" % time_total)
    print("")
    if error_total != 0:
        print("FAILURE (%d tests, %d failures)" % (test_total,error_total))
    else:
        print("OK (%d tests, %d assertions)" % (test_total,test_total))

def sample_testfile():
    print("""
url: "http://localhost"
tests:
- name: "Website is live"
  path: "/"
  request: "GET"
  expected_status: 200
""".strip())

def sample_headerfile():
    print("""
headers:
    - name: 'Authorization'
      value: 'Bearer [token]'
""".strip())


if __name__ == '__main__':
    import sys
    if '--sample' in sys.argv:
        sample_testfile()
        exit()
    if '--sample-header' in sys.argv:
        sample_headerfile()
        exit()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("test_script", help="Test script (.yaml)")
    parser.add_argument("--headers-script", help="Headers script, using name,value format (.yaml)")
    parser.add_argument("--sample", help="Show sample of tests YAML file")
    parser.add_argument("--sample-header", help="Show sample of headers YAML file")
    parser.add_argument('-i','--insecure',help='Do not verify SSL certificates (insecure)',action='store_true')
    parser.add_argument('-e','--errors',help='Show only errors',action='store_true')
    parser.add_argument("-t","--testsuite_file", help="Execute test scripts from testsuit YAML file",action="store_true")
    argv = parser.parse_args()
    vargs = vars(argv)
    if vargs.get("testsuite_file") != False:
        main_multiple(vargs)
    else:
        main(vargs)

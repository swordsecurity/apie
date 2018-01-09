#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os.path import dirname,realpath
import app.restbot.parser
import app.restbot.header_parser
import app.restbot.asserter
import app.restbot.tester
import time

def main(args):
    global_headers = {}
    if args.get('headers_script') is not None:
        global_headers = app.restbot.header_parser.parseFile(args['headers_script'])

    global_headers['Content-Type'] = 'application/json'

    testdata = app.restbot.parser.parseFile(args['test_script'])
    url = testdata['url']
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
        print("Test: %s" % test['name'])
        if(test_result):
            print("Result: OK")
        else:
            error_total += 1
            exp_type = list(expected.keys())[0]
            actual_type = 'actual_%s' % exp_type.replace('expected_','')
            expected[actual_type] = data
            print("Result: ERROR")
            print(expected)
        test_total += 1
        print("") #newline
    time_total = int(round((time.time()-time_begin) * 1000))

    print("Time: %d ms" % time_total)
    print("")
    if error_total != 0:
        print("FAILURE (%d tests, %d failures)" % (test_total,error_total))
    else:
        print("OK (%d tests, %d assertions)" % (test_total,test_total))


if __name__ == '__main__':
    import sys
    if '--sample-script' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/testfile.yaml",'r') as f:
            print(f.read())
            exit()
    if '--sample-header-script' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/headerfile.yaml",'r') as f:
            print(f.read())
            exit()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("test_script", help="Test script (.yaml)")
    parser.add_argument("--headers-script", help="Headers script, using name,value format (.yaml)")
    parser.add_argument("--sample-script", help="Show sample of tests YAML file")
    parser.add_argument("--sample-header-script", help="Show sample of headers YAML file")
    parser.add_argument('-i','--insecure',help='Do not verify SSL certificates (insecure)',action='store_true')
    argv = parser.parse_args()
    main(vars(argv))

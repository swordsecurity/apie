#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os.path import dirname,realpath
import app.restbot.parser
import app.restbot.header_parser
import app.restbot.asserter
import app.restbot.tester

def main(args):
    global_headers = {}
    if args.get('sample_header_script') is not None:
        global_headers = app.restbot.header_parser.parseFile(args['sample_header_script'])

    global_headers['Content-Type'] = 'application/json'

    testdata = app.restbot.parser.parseFile(args['test_script'])
    url = testdata['url']
    for item in testdata['tests']:
        test = item['test']
        expected = item['expected']
        test_result, data = app.restbot.tester.doTest(url,test,expected,global_headers)
        print("Test: %s" % test['name'])
        if(test_result):
            print("Result: OK")
        else:
            exp_type = expected.keys()[0]
            actual_type = 'actual_%s' % exp_type.replace('expected_','')
            expected[actual_type] = data
            print("Result: ERROR")
            print(expected)
        print("") #newline

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
    parser.add_argument("--sample-script", help="Show sample of tests YAML file")
    parser.add_argument("--sample-header-script", help="Show sample of headers YAML file")
    argv = parser.parse_args()
    main(vars(argv))

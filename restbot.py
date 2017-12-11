#!/usr/bin/python3
# -*- coding: utf-8 -*-
from os.path import dirname,realpath
import app.restbot.parser
import app.restbot.header_parser
import app.restbot.asserter
import app.restbot.tester

def main(args):
    global_headers = {}
    if args.get('header_file') is not None:
        global_headers = app.restbot.header_parser.parseFile(args['header_file'])

    global_headers['Content-Type'] = 'application/json'

    testdata = app.restbot.parser.parseFile(args['filename'])
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
    if '--example_script' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/testfile.yaml",'r') as f:
            print(f.read())
            exit()
    if '--example_header_file' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/headerfile.yaml",'r') as f:
            print(f.read())
            exit()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Test script (.yaml)")
    parser.add_argument("--header_file", help="Headers YAML file")
    parser.add_argument("--example_script", help="Show example tests YAML file")
    parser.add_argument("--example_header_file", help="Show example headers YAML file")
    argv = parser.parse_args()
    main(vars(argv))

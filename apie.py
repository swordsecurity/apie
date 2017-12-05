#!/usr/bin/python3
# -*- coding: utf-8 -*-

import apie.parser
import apie.header_parser
import apie.asserter
import apie.tester
from os.path import dirname,realpath

def main(args):
    global_headers = {}
    if args.get('header_file') is not None:
        global_headers = apie.header_parser.parseFile(args['header_file'])

    testdata = apie.parser.parseFile(args['file'])
    url = testdata['url']
    for item in testdata['tests']:
        test = item['test']
        expected = item['expected']
        test_result, data = apie.tester.doTest(url,test,expected,global_headers)
        if(test_result):
            print("OK",test['name'])
        else:
            expected['actual'] = data
            print("ERROR",test['name'],expected)

if __name__ == '__main__':
    import sys
    if '--example_test_file' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/testfile.yaml",'r') as f:
            print(f.read())
            exit()
    if '--example_header_file' in sys.argv:
        with open(dirname(realpath(__file__)) + "/tests/assets/headerfile.yaml",'r') as f:
            print(f.read())
            exit()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Tests YAML file")
    parser.add_argument("--header_file", help="Headers YAML file")
    parser.add_argument("--example_test_file", help="Show example tests YAML file")
    parser.add_argument("--example_header_file", help="Show example headers YAML file")
    argv = parser.parse_args()
    main(vars(argv))

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import yaml

def main(args):
    print(parseFile(args['file']))

def parseFile(filename):
    filename = os.path.realpath(filename)
    if not os.path.isfile(filename):
        raise Exception('file %s is not found' % filename)

    with open(filename) as f:
        dataMap = yaml.safe_load(f)

    if dataMap.get('headers') is None:
        raise Exception('headers attribute not found in %s' % filename)

    for header_info in dataMap['headers']:
        if header_info.get('name') is None:
            raise Exception('name attribute not found in %s' % filename)
        if header_info.get('value') is None:
            raise Exception('value attribute not found in %s' % filename)

    return dataMap['headers']

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="YAML configuration file")
    argv = parser.parse_args()
    main(vars(argv))

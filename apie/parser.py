#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import yaml

def main(args):
    print(parseFile(args['file']))

def parseFile(filename):
    data = {}
    if not os.path.isfile(filename):
        raise Exception('file %s is not found' % filename)

    with open(filename) as f:
        dataMap = yaml.safe_load(f)
    if dataMap.get('url') is None:
        raise Exception('url attribute not found in %s' % filename)

    if dataMap.get('tests') is None:
        raise Exception('tests attribute not found in %s' % filename)

    data['url'] = dataMap['url']
    data['tests'] = []
    for test in dataMap.get('tests'):
        for attribute in ['name','request','path']:
            if test.get(attribute) is None:
                raise Exception('%s attribute not found in %s' % (attribute,filename))

        expected = {}
        for exp in ['expected_status','expected_content','expected_value','expected_header']:
            if test.get(exp) is not None:
                exp_type = exp.replace('expected_','')
                exp_value = test.get(exp)
                expected[exp_type] = exp_value

        if len(expected) == 0:
            raise Exception("expected_* attribute not found in %s" % filename)

        data['tests'].append({'test':test,'expected':expected})

    return data

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="YAML configuration file")
    argv = parser.parse_args()
    main(vars(argv))

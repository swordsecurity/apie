#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main(args):
    import requests
    expected = {'content':args['content']}
    response = requests.get(args['url'])
    print(assert_response(response,expected))

def assert_response(response,expected):
    if expected.get('expected_status') is not None:
        result = expected['expected_status'] == response.status_code
        data = response.status_code
    elif expected.get('expected_content') is not None:
        result = expected['expected_content'].lower() in response.text.lower()
        data = response.text.lower()
    elif expected.get('expected_value') is not None:
        result = expected['expected_value'] == response.text
        data = response.text
    else:
        raise Exception('Expected is not expected_status,expected_content or expected_value')

    return result,data

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to site")
    parser.add_argument("content", help="content on site")
    argv = parser.parse_args()
    main(vars(argv))

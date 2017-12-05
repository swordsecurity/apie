#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import main

import sys
from os.path import dirname,realpath
sys.path.append(dirname(dirname(realpath(__file__))))
import apie.header_parser

class test_header_parser(TestCase):

    def test_parser_file(self):
        filename = dirname(realpath(__file__)) + "/assets/headerfile.yaml"
        apie.header_parser.parseFile(filename)
        self.assertTrue(True)

    def test_parser_file_without_headers(self):
        filename = dirname(realpath(__file__)) + "/assets/headerfilewithoutheaders.yaml"
        result = None
        expected = 'headers attribute not found in %s' % filename
        try:
            apie.header_parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_file_without_header_name(self):
        filename = dirname(realpath(__file__)) + "/assets/headerfilewithoutheadername.yaml"
        result = None
        expected = 'name attribute not found in %s' % filename
        try:
            apie.header_parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_file_without_header_value(self):
        filename = dirname(realpath(__file__)) + "/assets/headerfilewithoutheadervalue.yaml"
        result = None
        expected = 'value attribute not found in %s' % filename
        try:
            apie.header_parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

if __name__ == '__main__':
    main()

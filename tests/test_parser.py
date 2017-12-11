#!/usr/bin/python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest import main

import sys
from os.path import dirname,realpath
sys.path.append(dirname(dirname(realpath(__file__))))
import app.restbot.parser

class test_parser_file(TestCase):

    def test_parser_file(self):
        filename = dirname(realpath(__file__)) + "/assets/testfile.yaml"
        app.restbot.parser.parseFile(filename)
        self.assertTrue(True)

    def test_parser_filewithouturl(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithouturl.yaml"
        result = None
        expected = 'url attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_filewithouttests(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithouttests.yaml"
        result = None
        expected = 'tests attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_filewithoutpath(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithoutpath.yaml"
        result = None
        expected = 'path attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_filewithoutname(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithoutname.yaml"
        result = None
        expected = 'name attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

    def test_parser_filewithoutexpected(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithoutexpected.yaml"
        result = None
        expected = 'expected_* attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)


    def test_parser_filewithoutrequest(self):
        filename = dirname(realpath(__file__)) + "/assets/filewithoutrequest.yaml"
        result = None
        expected = 'request attribute not found in %s' % filename
        try:
            app.restbot.parser.parseFile(filename)
        except Exception as e:
            result = str(e)

        self.assertEqual(expected,result)

if __name__ == '__main__':
    main()

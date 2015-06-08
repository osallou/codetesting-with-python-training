from nose.tools import *
from nose.plugins.attrib import attr


from mysamplecode.samplecode import SampleCode
import mock
from mock import patch
import logging

import unittest



class Test(unittest.TestCase):


    def setUp(self):
        self.counter = 0

    def tearDown(self):
        pass

    @attr('count')
    def testAdd(self):
        sample = SampleCode()
        result = sample.add(1,1)
        self.assertEqual(2, result)

    def testAuthenticate(self):
        sample = SampleCode()
        is_auth = sample.authenticate('sampleuser', 'yy')

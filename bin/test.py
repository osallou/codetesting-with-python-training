#!/usr/bin/env python

import logging

from mysamplecode.samplecode import SampleCode

logging.warn("Start example program: 1+3")

sample = SampleCode()

result = sample.add(1,3)

logging.warn("Result: "+str(result))

#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

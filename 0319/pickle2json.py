#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import json
d = dict(name='ZhangLingmei', age=23, socre=90)
f = open('json_dump.txt', 'w')
str = json.dumps(d)
f.write(str)
print(str)
print('ok')

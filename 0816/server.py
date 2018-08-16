#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

from hello import application

# create a server ip is empty port is 8000, process function is application
httpd = make_server('', 8000, application)
print('Sever HTTP on port 8000...')

# start listern HTTP Request
httpd.serve_forever()

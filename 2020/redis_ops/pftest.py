# /usr/bin/env python3
# coding: utf-8

import redis

client = redis.StrictRedis(host='192.168.10.10', port=6379, db=0)
for i in range(100000):
    client.pfadd("codehole", "user%d" % i)
print(100000, client.pfcount("codehole"))
print("Ok!\n")


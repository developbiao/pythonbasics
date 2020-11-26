# /usr/bin/env python3
# coding: utf-8

import redis

client = redis.StrictRedis(host='192.168.10.10', port=6379, db=0)
for i in range(1000):
    client.pfadd("codehole", "user%d" % i)
    total = client.pfcount("codehole")
    if total != i + 1:
        print(total, i + 1)
        break


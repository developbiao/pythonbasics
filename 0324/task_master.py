#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# Send task queue
task_queue = queue.Queue()
# Resive result queue
result_queue = queue.Queue()

# BaseManager extend QueueManager:
class QueueManager(BaseManager):
    pass

# Tow Queue resiter to network, callbale argments assoc queue object:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# bind port 5000, seting authkey is 'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')

# start Queue:
manager.start()

# get Queue object by network
task = manager.get_task_queue()
result = manager.get_result_queue()

# put task
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# get result
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

# close:
manager.shutdown()
print('masger exit.')

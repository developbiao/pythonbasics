#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# Create QueueManager:
class QueueManager(BaseManager):
    pass

# Because this QueueMnager get Queue from network so just provid register name:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# connect to server(masgter)
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# give port and authkey
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# connect
m.connect()
# get Queue Object
task = m.get_task_queue()
result = m.get_result_queue()

# get task from queue, and result write to queue:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')

# process over
print('worker exit.')

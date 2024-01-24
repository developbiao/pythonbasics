# -*- coding: utf-8 -*-

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    case ['gcc']:
        print('gcc: missing source files(s).')
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', ' . join(files))
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')


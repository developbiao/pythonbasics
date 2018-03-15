#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Screen(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

   
print("==== start test screen resolution ====")
s = Screen(1366, 768)
if s.resolution == 1049088:
    print("测试通过PASS!")
else:
    print("测试失败!")



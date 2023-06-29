#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

from PIL import Image
import numpy as np 
im = Image.open('roll_over.jpg')
print(im.size)

im_pillow = np.asarray(im)

print(im_pillow.shape)




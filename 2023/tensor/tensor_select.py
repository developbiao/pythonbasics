#!/usr/bin/env python3
#!-*- coding:utf-8 -*-

import torch

A = torch.tensor([[4, 5, 7], [3, 9, 8], [2, 3, 4]])
mask = torch.tensor([[1, 0, 0], [1, 1, 0], [0, 0, 1]])
B = torch.masked_select(A, mask > 0)
print(B)


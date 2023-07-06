#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
from torch.utils.data import DataLoader

my_dataset = torch.randn(3, 10)
tensor_dataloader = DataLoader(dataset = my_dataset,
        batch_size=2,
        shuffle=True,
        num_workers = 0)

for data, target in tensor_dataloader:
    print(data, target)

# output one batch !bug
# object has no attribute 'next'
print('One batch tensor data: ', iter(tensor_dataloader).next())


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torch
from torch.utils.data import Dataset

class MyDataset(Dataset):
    # constrcut
    def __init__(self, data_tensor, target_tensor):
        self.data_tensor = data_tensor
        self.target_tensor = target_tensor

    # length
    def __len__(self):
        return self.data_tensor.size(0)

    # get item by index
    def __getitem__(self, index):
        return self.data_tensor[index], self.target_tensor[index]


# Generate data
data_tensor = torch.randn(10, 3)
target_tensor = torch.randint(2, (10,))

# MyDataset object
my_dataset = MyDataset(data_tensor, target_tensor)

# Show data size
print('Dataset size:', len(my_dataset))

# Get data by index
print('tensor_data[0]: ', my_dataset[0])




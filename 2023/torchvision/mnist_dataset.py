#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import torchvision
from PIL import Image

mnist_dataset = torchvision.datasets.MNIST(root='/mnt/d/workspace/model/data',
                                            train=True, 
                                            transform=None,
                                            target_transform=None,
                                            download=False)

mnist_dataset_list = list(mnist_dataset)
#print(mnist_dataset_list)
display(mnist_dataset_list[0][0])
print("Image label is:", mnist_dataset_list[0][1])





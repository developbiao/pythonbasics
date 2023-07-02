#!/usr/bin/env python3

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [32, 64, 71, 89]
bubble_sort(arr)
print("Sorted a array:", arr)

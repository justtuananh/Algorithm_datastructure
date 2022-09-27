from random import seed
import time
from numpy import random
import pandas as pd 
import statistics
import time
import numpy as np 
random.seed(42)
from selectionSort import selectionSort
from bubbleSort import bubbleSort 
from quickSort import quickSort 
from insertSort import insertionSort

# # khoảng giá trị lấy của mảng
# n = int(input("input n( n must be a multiple of 10):"))
# # số giá trị của mảng 
# sizeArr =int(input("input sizeof array:"))


# arr=random.randint(1000, size=(10000))


def tol_time(l, start_index, end_index):
  total = 0
  for val in (l[start_index: end_index]):
    total = (total + val)
  std_times  =statistics.stdev(l[start_index: end_index])
  return round(total/50,5) ,round(std_times,5)


insertion_time = []
bubble_time = []
quick_time = []
selection_time = []

for n in([10,100,1000]): #for n in(n_size):   
    for i in range(0, 50) :
        start_time = time.time()
        arr = np.random.randint(10000, size = n)
        insertionSort(arr)
        end_time = time.time()            
        insertion_time.append(end_time - start_time)

#time calculations for insertion sort

#n_size =10
ins_time1 = tol_time(insertion_time, 0,50)
ins_time1 = " +/- ".join([i for i in map(str, ins_time1)])

#n_size =100
ins_time2 = tol_time(insertion_time,51,100)
ins_time2 = " +/- ".join([i for i in map(str, ins_time2)])

n_size = 1000
ins_time3=tol_time(insertion_time,101,150)
ins_time3 = " +/- ".join([i for i in map(str, ins_time3)])

#write into a list with round to 5 number
Insertion = []
Insertion.extend((ins_time1, ins_time2, ins_time3))


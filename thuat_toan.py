from tracemalloc import Statistic
from numpy import random

import time 
import statistics 
timess = []
for i in range(30): 
    start_time = time.time()

    def insertionSort(arr):

        for i in range(1, len(arr)):
    
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
    

    def bubbleSort(arr):
 
     for i in range(len(arr)):
 
        # Last i elements are already in place
        for j in range(0, len(arr)-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
    # Python program for implementation of Selection
# Sort


# Traverse through all array elements
for i in range(len(arr)):
	
	# Find the minimum element in remaining
	# unsorted array
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[min_idx] > arr[j]:
			min_idx = j
			
	# Swap the found minimum element with
	# the first element	
	arr[i], arr[min_idx] = arr[min_idx], arr[i]


    arr = random.randint(100000, size=(10000))
    insertionSort(arr)
    bubbleSort(arr)
 


    print("--- %s seconds ---" % (time.time() - start_time))
    timess.append(time.time() - start_time)

print("Mean : ")
print(statistics.mean(timess))
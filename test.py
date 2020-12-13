from copy import copy
from timeit import timeit
from bubblesort_caller import c_sort
from bubblesort import py_sort
from random import seed, randint
from time import time
import sys
import array

if len(sys.argv) < 2:
	print("[ERROR] You should pass array size as an argument");
	sys.exit()

try:
    size = int(sys.argv[1])
except (ValueError, TypeError):
    print("[ERROR] Failed to read program argument as integer")
    sys.exit()

if size <= 0:
    print("[ERROR] Array size should be positive integer")

ms_in_sec = 1000
seed(time())

arr = []
for i in range(size):
    value = randint(-1000, 1000)
    arr.append(value)

arr1 = array.array('i', arr)
arr2 = copy(arr1)

dur = timeit(lambda: c_sort(arr1, size), number=1)
print("c bubble sort:", round(dur * ms_in_sec, 1), "ms")

dur = timeit(lambda: py_sort(arr2, size), number=1)
print("python bubble sort:", round(dur * ms_in_sec, 1), "ms")

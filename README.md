# cython-sort-test
Small project to test performance of bubble sort in **Python 3.7** with and without **Cython**. It can be helpful if you're curious about how to work with arrays in **Cython**. 
## Building
Make sure you have **Cython** installed, otherwise do `pip install Cython`
1. `python setup.py build_ext --inplace`
2. `python setup.py clean -all`

## Run
Run with `python test.py [size]`\, where [size] is the size of array filled with random integers from -1000 to 1000 that is being sorted.

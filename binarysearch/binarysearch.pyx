
cimport cython
from libc.stdlib import malloc

cdef extern from "binarysearch.h":
    int binary_search(int collection[], int length, int target)

def _search(collection, length, target):
    array = <int *>malloc(len(collection)*cython.sizeof(collection))
    for i in xrange(len(collection)):
        array[i] = collection[i]
    return binary_search(array, length, target)

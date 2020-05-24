from cpython cimport array
import array

cdef extern from "binarysearch.h":
    int binary_search(int collection[], int length, int target)

def _search(list collection, length, target):
    cdef array.array list = array.array('f', collection)
    return binary_search(list.data.as_ints, length, target)

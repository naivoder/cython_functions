cdef extern from "swapbits.h":
    int swap_bits(int word, int i, int j)

def _swap(word, i , j):
    return swap_bits(word, i, j)

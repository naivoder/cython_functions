import swapbits

if __name__=="__main__":
  print("###---Swap Bits with Cython---###")
  print("Given: 1111, 'i': 2, 'j': 2")
  swapbits._swap(1111, 2, 3)

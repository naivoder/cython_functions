import binarysearch, random

if __name__=="__main__":
  print("###---Binary Search with Cython---###")
  test_data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  print(test_data)
  print(len(test_data))
  binarysearch._search(test_data, 20, 19)

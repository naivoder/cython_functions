#include <stdio.h>
#include "binarysearch.h"

int binary_search(int collection[], int length, int target) {
  int left = 0, right = length - 1;
  while (left <= right) {
    int midpoint = (left + right) / 2;
    if (collection[midpoint] == target) {
      printf("Found at %d\n", midpoint);
      return midpoint;
    } else if (collection[midpoint] < target) {
      left = midpoint + 1;
    } else {
      right = midpoint - 1;
    }
  }
  printf("Not found :(\n");
  return -1;
}

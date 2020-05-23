#include <stdio.h>
#include <stdlib.h>
#include "swapbits.h"

int swap_bits(int word, int i, int j) {
	int hold = word;
	int bit_mask;
  if (((word >> i) & 1) != ((word >> j) & 1)) {
    bit_mask = (1 << i) | (1 << j);
    word ^= bit_mask;
  }
	printf("Result: %d\n", word);
  return word;
}

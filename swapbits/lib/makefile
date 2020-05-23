CC = gcc

default: libswapbits.a

libswapbits.a: swapbits.o
	ar rcs $@ $^

swapbits.o: swapbits.c swapbits.h
	$(CC) -c $<

clean:
	rm *.o *.a

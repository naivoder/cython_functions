CC = gcc

default: libbinarysearch.a

libbinarysearch.a: binarysearch.o
	ar rcs $@ $^

binarysearch.o: binarysearch.c binarysearch.h
	$(CC) -c $<

clean:
	rm *.o *.a

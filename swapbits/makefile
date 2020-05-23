LIB_DIR = lib

default: swapbits

swapbits: setup.py swapbits.pyx $(LIB_DIR)/libswapbits.a
	python3 setup.py build_ext --inplace && rm -f swapbits.c && rm -Rf build

$(LIB_DIR)/libswapbits.a:
	make -C $(LIB_DIR) libswapbits.a

clean:
	rm *.so

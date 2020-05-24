LIB_DIR = lib

default: binarysearch

binarysearch: setup.py binarysearch.pyx $(LIB_DIR)/libbinarysearch.a
	python3 setup.py build_ext --inplace && rm -f binarysearch.c && rm -Rf build

$(LIB_DIR)/libbinarysearch.a:
	make -C $(LIB_DIR) libbinarysearch.a

clean:
	rm *.so

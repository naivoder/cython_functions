from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

binarysearch_extension = Extension(
    name="binarysearch",
    sources=["binarysearch.pyx"],
    libraries=["binarysearch"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)
setup(
    name="binarysearch",
    ext_modules=cythonize([binarysearch_extension])
)

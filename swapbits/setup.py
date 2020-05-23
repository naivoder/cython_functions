from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

bitswap_extension = Extension(
    name="swapbits",
    sources=["swapbits.pyx"],
    libraries=["swapbits"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)
setup(
    name="swapbits",
    ext_modules=cythonize([bitswap_extension])
)

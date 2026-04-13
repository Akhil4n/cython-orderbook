from setuptools import setup, find_packages
from Cython.Build import cythonize
import os

# Use .pyx if Cython is available, otherwise fall back to .c
if os.path.exists("cython_orderbook/orderbook.pyx"):
    from Cython.Build import cythonize
    ext_modules = cythonize("cython_orderbook/orderbook.pyx", compiler_directives={
        "language_level": "3",
    })
else:
    from setuptools import Extension
    ext_modules = [Extension("cython_orderbook.orderbook", ["cython_orderbook/orderbook.c"])]

setup(
    packages=find_packages(),
    ext_modules=ext_modules,
)
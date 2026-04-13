from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    packages=find_packages(),
    ext_modules=cythonize("cython_orderbook/orderbook.pyx", compiler_directives={
        "language_level": "3",
    })
)
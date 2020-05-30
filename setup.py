from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("fibonacci_python_with_cpp.pyx")
)

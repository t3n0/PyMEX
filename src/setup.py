#-------------------------------------------------------------------------
#
# This is similar to a setup.py file and performs the same task as the command
#
#   cythonize -i -a <mymodule>.pxy
#
# We need this to cythonize the .pyx module to .c modules.
# This is useful because we can specify compiler flags such as "-fopemp"
# (I actually didn't find out how to add -fopenmp to the cytonize command)
#
# To compile, run:
#
#   python cythonize.py build_ext --inplace
#
#-------------------------------------------------------------------------

from setuptools import Extension, setup
from Cython.Build import cythonize

myextensions = [
    Extension(
        name    = "cyfunc",
        sources = ["cyfunc.pyx"],
        extra_compile_args = ['-fopenmp'],
        extra_link_args    = ['-fopenmp']
        )
    ]

setup(
	ext_modules = cythonize(
	    myextensions,
	    annotate = True,
	    language_level ="3str"
	    )
	)


# from distutils.core import setup, Extension
# from Cython.Build import cythonize
# import os
# #os.environ["CC"] = "clang"
# #os.environ["CXX"] = "clang++"

# extensions = [Extension(
#                 "cyfunc",
#                 sources=["cyfunc.pyx"],
#                 #extra_compile_args=["-fopenmp", "-Wunreachable-code-fallthrough","-Wno-unreachable-code"],
#                 extra_compile_args=["-fopenmp", "-Wno-unreachable-code"],
#                 extra_link_args=["-fopenmp"]
#             )]

# setup(
#     ext_modules = cythonize(extensions)
# )


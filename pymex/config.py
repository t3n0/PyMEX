'''
Configuration file for global variables, constants and utilities
used over the whole project.
'''

from mpi4py import MPI
from functools import partial
import os

# MPI initialisation
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
root = 0

# print flush definition
print_f = partial(print, flush=True)

# current working directory
CWD = os.getcwd()

# physical constants
Bohr_to_Ang = 0.52917720859

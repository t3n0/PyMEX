import sys
sys.path.append("/home/tentacolo/Documents/Physics/Projects/PyMEX/src")
from bse import BSE
import time
from functools import partial
print_f = partial(print, flush=True)
import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
root = 0

#------------
# Calculations
#-------------
t1 = time.time()
BSE = BSE("pymex.inp")
BSE.write_Ham_parallel()
BSE.diagon_BSE()

#---------------
if rank == root:
  print_f("Time taken on %d processes :%.3f secs."%(size,\
       time.time()-t1))

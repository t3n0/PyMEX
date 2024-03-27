from config import *
from bse import BSE
import time


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

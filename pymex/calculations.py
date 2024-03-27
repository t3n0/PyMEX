#-----------------------------|
#email: i.maity@imperial.ac.uk|
#Author: Indrajit Maity       |
#-----------------------------|

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
BSE.sigma_xx()

#Plotting etc.
# S, c, v
#BSE.plot_exciton_k(0,0,0)
#BSE.plot_exciton_k(1,0,0)
#BSE.plot_exciton_k(2,0,0)
#BSE.plot_exciton_k(3,0,0)
#BSE.plot_exciton_k(4,0,0)
#BSE.plot_exciton_k(5,0,0)
#---------------
if rank == root:
  print_f("Time taken on %d processes :%.3f secs."%(size,\
       time.time()-t1))

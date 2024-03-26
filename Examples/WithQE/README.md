# Usage of PyMEX with Quantum Espresso

**Author: Indrajit Maity  
Email: <indrajit.maity02@gmail.com>**

Example to solve the BSE with PyMEX for a relatively coarse grid.  
NOTE: The spin-orbit coupling is included in the electronic
structure calculations explicitly. This is a non-perutbative
calculation. For a perturbative treatment, see the example
[WithSiesta](../WithSiesta).

YOU MUST change the number of orbital within the
`wan90tobse.py` to 10 for W and 6 for Se. Will be automated
in the future!


Input file description:

1. wannier90 input file (link)
2. QE input file (link)

Workflow:


1. Run the QE workflow

   ```
   mpirun -n 4 pw.x -in scf.in >> scf.out
   mpirun -n 4 pw.x -in nscf.in >> nscf.out
   mpirun -n 4 bands.x -in bands.in >> bands.out
   ```

   We obtain the DFT ground state and the desired number bands for the wannierization.  
   Also, the `nscf` calculation must be performed with `nosym=true`: we need to input all the kpoint explicitly.

2. Run wannier preprocessing tool `wannier90.x -pp`

   ```
   mpirun -n 4 wannier90.x -pp WSe2
   ```

   This generates the `WSe2.nnkp`.

3. Run the interface code 
   ```
   mpirun -n 4 pw2wannier90.x -in WSe2.pw2wan >& pw2wan.out
   ```

4. Run a one-shot projection calculation with `num_iter = 0`
   ```
   mpirun -n 4 wannier90.x -in WSe2
   ```

5. (optional) Re-run wannier90 with the option `restart = [default | wannierise | plot]` if you need to compute some other quantities or plots
   ```
   mpirun -n 4 wannier90.x -in WSe2
   ```

6. Run `PyMEX` to construct the hamiltonian and to perform the absorption calculation
   ```
   mpirun -n 4 python calc_Ham.py >& ham.out
   mpirun -n 4 python calc_Absorb.py >& abs.out
   ```

Note1: use the `kmesh.pl` tool in the wannier folder to generate the explicit list of kpoints needed by the nscf and wannier itself.
```
./kmesh 4 4 1 >> kpoints
```

Note2: it might be worth to use the `-pd .true.` and `-nk <k>` parallelisation flags in certain situations.
```
mpirun -n 4 pw.x -pd .true. -nk 3 -in scf.in > scf.out
mpirun -n 4 bands.x -pd .true. -in bands.in > bands.out
mpirun -n 4 pw2wannier90.x -pd .true. -in WSe2.pw2wan >& pw2wan.out
```

Note3: Ideally, the numprocess can be anything <= Numberofkpoints x NumberofValencebands x NumberofCondbands; In this case, it is= 9 x 9 x 2 x 2 = 324. However, we found the h5py-parallel works only for a integer divisor of Numberofkpoints x Numberofbands. Therefore, the numprocess here can be 1, 2, 3, 4, 6, etc. upto 324. However, if you enter 5 as numprocess the code will throw an error!

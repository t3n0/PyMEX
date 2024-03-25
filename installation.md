# Installation (Linux)

PyMEX requires a number of libraries and tools to operate.  
The installation steps are the following:

1. install `python` and the required libraries;
2. install `wannier90`;
3. install `quantum espresso`;
4. compile, build and install `PyMEX`.

## 1. Python installation
<details><summary> Click to expand </summary>

The easiest way install python and the required dependencies is with `conda`.

- Download and install miniconda:

   ```
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh
   ```

- Type `yes` agree license, ok default folder, `yes` conda init.

- Update conda, add the `conda-forge` channel and create a new environment:

   ```
   conda update conda
   conda config --add channels conda-forge
   conda create -n pymex
   conda activate pymex
   ```

- Finally, install the required libraries

   ```
   conda install "h5py>=2.9=mpi*"
   conda install scipy
   conda install cython
   ```

Note1: installing `h5py` with mpi support will install `numpy` and `mpi4py` automatically.

Note2: you can specify the mpi flavour, either `openmpi` or `mpich`, by typing it excplicitly in the command: `"h5py>=2.9=mpi_mpich*"`.

</details>

## 2. Wannier90 installation

<details><summary> Click to expand </summary>

A super straight forward guide to instal [Wannier90](https://wannier.org/) on Ubuntu.  
The complete installation guide is [here](https://github.com/wannier-developers/wannier90/blob/develop/README.install).

1. Install `blas` and `lapack` libraries
   
   ```bash
   sudo apt install libblas-dev liblapack-dev
   ```
2. Install an MPI implementation: either `mpich` or `openmpi`
   ```bash
   sudo apt install mpich
   ```
3. Install `gfortran`, aka the gcc f90 compiler
   ```bash
   sudo apt install build-essential gfortran
   ```
4. Check GNU make version, e.g. `GNU Make 4.2.1`
   ```bash
   make -v
   ```
5. [Download](https://wannier.org/download/) the latest wannier90 (older versions [here](https://github.com/wannier-developers/wannier90/tags))
6. Unzip the folder at you favorite location and create a `make.inc` file with the following content
   ```
   #===================
   # gfortran
   #===================
   F90 = gfortran

   COMMS  = mpi
   MPIF90 = mpif90

   FCOPTS = -O3
   LDOPTS =

   #Next two lines are good for debugging
   #FCOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace
   #LDOPTS = -fstrict-aliasing  -fno-omit-frame-pointer -fno-realloc-lhs -fcheck=bounds,do,recursion,pointer -ffree-form -Wall -Waliasing -Wsurprising -Wline-truncation -Wno-tabs -Wno-uninitialized -Wno-unused-dummy-argument -Wno-unused -Wno-character-truncation -O1 -g -fbacktrace

   #=======================
   # System LAPACK and BLAS
   #=======================
   LIBS = -llapack -lblas
   ```
7. Open the terminal in the base folder and run the following (this builds `wannier90.x` and `postw90.x` executables only)
   ```bash
   make default
   ```
8. (optional) Add `wannier90.x` and `postw90.x` to the PATH, so that they can run system-wide. Do **either**
   - add to `bin`
     
     ```bash
     ln -s /path/to/wannier/folder/wannier90.x /usr/local/bin/wannier90.x
     ln -s /path/to/wannier/folder/postw90.x   /usr/local/bin/postw90.x
     ```
   - add to PATH: append this line to `.bashrc`
     ```bash
     export PATH="/path/to/wannier/folder:$PATH"
     ```

</details>

## 3. Install Quantum Espresso

<details><summary> Click to expand </summary>

1. Install `blas`, `lapack` and `fftw3` libraries
   
   ```bash
   sudo apt install libblas-dev liblapack-dev libfftw3-dev
   ```

2. [Download](https://www.quantum-espresso.org/download-page/) the latest Quantum Espresso (requires login). Save it in your favourite directory and unzip it.

3. Move into the folder and run
    ```
    ./configure
    make all
    ```

4. (optional) Export the executable to the PATH. Add the following to `.bashrc`
    ```bash
    export PATH="</path/to/qe-x.y/bin>:$PATH"
    ```

Note1: you can customize the installation by passing several options to the `./configure` script. Type the following for an explanation of all options:
```
./configure --help
```

Note2: Similarly, to customize the tools you want to install, just type
```
make
```
and this will list all the available make options.

</details>

## 4. Compile, build and install PyMEX

<details><summary> Click to expand </summary>

</details>

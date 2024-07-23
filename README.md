## About
This repository contains all the codes associated with the paper *Variational numerical-modelling strategies for the simulation of driven free-surface waves*, where we revisit the [3D wave tank test cases (TCs)](https://github.com/EAGRE-water-wave-impact-modelling/3D-wave-tank-JCP2022) through the "VP-based approach"; the weak formulations are now generated automatically and implemented implicitly based on a time-discretised VP onto which [*Firedrake*](https://www.firedrakeproject.org/)'s `derivative()` functionality applies. 

To compare the results with the old ones, some changes are also made to the original code, where manually derived weak formulations for the SE and SV schemes are explicitly formulated in *Firedrake*.

Regarding TC5 simulation, please see readme in TC5_codes.

## Computation Codes
- Main file:
    - The new approach: `3D_tank_VP.py`
    - The old approach: `3D_tank.py`
- Shared files:
    - Settings of TCx: `settings_TCx.py`
    - Save the job details: `savings.py`
- Exclusive to the old approach:
    - Explicit weak formulations for SE and SV in `solvers_full.py`

## Developing Notes
- In `settings.py`, how the wavemaker-related functions update against time has been changed.
- In `3D_tank.py`, which uses the 'old approach', the Lagrange polynomial $\tilde{\varphi}_i(z)$ is now constructed based on GLL points.
- In `3D_tank_VP.py`, $\hat{\phi}(z)$ can be switched between 1 and high order Lagrange polynomial based on GLL points via the flag `hatphi_one`; while the flag `one_ver_ele` decides whether there is only one element or multiple elements for the discretisation in the $z$-direction.
- In `3D_tank_VP.py`, the field data is now evaluated at a matrix of points via `VertexOnlyMesh`, and it's parallel safe.
- Saving results into files:
    - TC1/TC2: `energy.csv` containing time series of energy of the fluid domain, a series of `.npy` binary files containing 1D field data named after the time step, and `readme.txt`, which is a summary of the settings for the simulation;
    - TC3: `checkpoints.csv` containing energy, water depths at three vertices and wavemaker-related data, `readme.txt`;
    - TC4: `energy.csv`, `probes.csv` with numerical measurements, `readme.txt`.

## Simulation Instructions
1. Specify which test case you are going to run by changing `case = 'TCx'`  at the start of the main file (`3D_tank_VP.py` or `3D_tank.py`).
1. Setting the parameters for a particular simulation in `settings.py`:
    1. Specify the directory where the numerical results will be stored by changing the `save_path` in `settings_TCx.py`.
    2. Adjust the spatial resolution via `res_x`, `res_y` and `nz` in the function `domain`; change the temporal resolution via `dt` in the function `set_time`.
1. When a simulation finishes, check the output files in the directory you specified in step 1. The numerical results can be processed and visualised with the post-processing codes provided in the folder [post-processing](post-processing).

**HPC Notes:**
- If you are going to carry out the simulations on an HPC, please ensure that you have requested an acceptable amount of time and memory in the job submission script. These can be determined by trial and error. It is useful to retrieve the data of a job run via the command `qacct -j JOBID` and check the maximum memory and time actually used from the rows `maxvmem` and `ru_wallclock`. You can then update your resource request lines in your job submission script to prevent the job from being aborted in the future.
- Two example job submission scripts, one for using the processes on a single node (`MPI_SingleNode.sh`) and the other for running anywhere (`MPI_Anywhere.sh`), are provided here. The cache will be using different storage places but not the home directory. For single-node jobs, extra local disk space needs to be explicitly requested for the cache.

## Appendix: Records of TCs
| Test Case | New Approach (MMP-VP) | Old Approach (SV-GLL) |
| :---:     |    :----:    |   :----:     |
| TC1/2 |**`3D_tank_VP.py`** <br/>`settings_TC1/2.py`, `savings.py` | **`3D_tank.py`** + `solvers_full.py` <br/>`settings_TC1/2.py`, `savings.py`  |
| TC3       |**`3D_tank_VP.py`** <br/>`settings_TC3.py`, `savings.py`<br/> :white_check_mark: Δt=0.001s: Done. 22h(16p-YL); <br/> :white_check_mark: Δt=0.002s: Done. 11h(16p-YL)/24h(32p-HPC) | **`3D_tank.py`** + `solvers_full.py` <br/>`settings_TC3.py`, `savings.py` <br/> :white_check_mark: Δt=0.001s: Done. 15h(16p-YL); <br/> :white_check_mark: Δt=0.002s: Done. 7h(16p-YL). |
| TC4       |**`3D_tank_VP.py`** <br/>`settings_TC4.py`, `savings.py`<br/> folder [202002](202002) <br/> :white_check_mark: Done. 28h(16p-YL). 20240108 |  **`3D_tank.py`** + `solvers_full.py`<br/>`settings_TC4.py`, `savings.py` <br/> folder [202002](202002) <br/> :white_check_mark: Done. 26h(16p-YL). 20240113  |
| TC5       |**`pot_sp2.py``PFE_sp2max.py`,** <br/> `PFE_sp2maxA.py`, `PFE_sp2A.py`, `PFE_sp2energy.py`<br/> folder TC5_codes <br/> :white_check_mark: Done. 20240724

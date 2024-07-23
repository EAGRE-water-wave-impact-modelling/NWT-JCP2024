# User instructions

Program that solves the Potential Flow Equations (PFE) on a 3D periodic domain using the modified mid-point scheme.

The simulation tracks the evolution of three line solitons as they interact, 
to produce an eight times higher splash than the initial height of each soliton.

## FILES

The code consists of five files:
- `pot_sp2.py` is the main file that solves PFE;
- `PFE_sp2energy.py`, `PFE_sp2max.py`, `PFE_sp2A.py`, and `PFE_sp2_maxA.py` are used for plotting the evolution of energy and maximum, amplitude of solitons in a far field (denoted by A), and maximum divided by A, respectively.

After the computation of `pot_sp2.py` is finished, four sets of data are produced:
- solutions eta and Phi in "*data/height.pvd*", "*data/psi.pvd*", "*data/varphi.pvd*";
- evolution of energy and maximum against time is saved in "*data/potflow3dperenergy.txt";


The computational data can be visualised as follows:
- Solutions eta and Phi are pvd files that can be read with Paraview.
- Time evolution of energy can be plotted by running file `PFE_sp2energy.py`.
- Time evolution of maximum of eta can be plotted by running file `PFE_sp2max.py`.
- Time evolution of A can be plotted by running file `PFE_sp2A.py`.
- Time evolution of maximum/A can be plotted by running file `PFE_sp2maxA.py`.

We provide a table in which parameters were uses for setting simulations as follows. We denote spatial resolution by $\Delta x\approx\Delta y=965.4/97$. $T$ is the total simulation time defined as $T=t_{end}-t_{0}$ with $t_0=0{\rm s}$. $\Delta t=0.2856{\rm s}$ or $\Delta t_{BLE}=0.01$.  In order to change order of basis, modify nCG (currently setting nCG=2). For $N_y$, modify multiple (currently setting mutiple=1), for $\Delta t_{BLE}$, modify mutiple2(currently setting multiple2=1).  All simullations were given the same parameters as follws: $\epsilon=0.05$, $\mu=\epsilon^2$, $\delta=10^{-5}$, $L_x=965.4 (m)$, $L_y=4845.7 (m)$, $L_z=20 (m)$ $T=1428.0 (s)$. All simuations were run on 40 cores of Leeds' arc4-HPC. The table below appears within the caption of fig.13.
  
Simulation  |$\Delta t_{BLE}$ | $N_x$ | $N_y$ |$N_z$|DoFs |Run time (min)  
:---        | :---      | :---    | :---       | :----     |:----           |:---      | :---           | :---    |:---   |:---| :---|:---
PFE: CG2/ $\frac{\Delta y}{3}$ / $\Delta t$ |0.005  | 226 | 600 | 4|5,750,388|2880
PFE: CG4/ $\frac{2\Delta y}{3}$ / $\Delta t$ |0.005  | 133 | 300 | 4|5,750,388|5588
PFE: CG2/ $\frac{\Delta y}{4}$ / $\Delta t$ |0.005  | 355 | 800 | 4|10,230,390|5383
PFE: CG2/ $\frac{\Delta y}{3}$ / $\frac{\Delta t}{2}$ |0.0025  | 226 | 600 | 4|5,750,388|6094.6
BLE: CG2/ $\frac{\Delta y}{3}$ / $\Delta t$ |0.005  | 226 | 600 |-- |--|396

## Reference

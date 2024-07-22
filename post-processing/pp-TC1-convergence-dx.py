
import numpy as np
from numpy.linalg import norm
from matplotlib import pyplot as plt
import os.path

# -------------------------------------------------------------------------
Lx = 2*np.pi

data_path = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx3200_nz64_dtf'
data_path1 = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx800_nz32_2dtf'
data_path2 = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx400_nz32_2dtf'
data_path3 = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx200_nz32_2dtf'
data_path4 = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx100_nz32_2dtf'
data_path5 = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/Nx50_nz32_2dtf'
dx = np.array([Lx/800, Lx/400, Lx/200, Lx/100, Lx/50])

one_point = True
results = 'psi' #'h/psi'
save_figure = True
figure_name = 'error-dx('+results+').png'
# -------------------------------------------------------------------------

if save_figure:
    path = 'data_VP/MMP/TC1_2D_series2(1ele,phiGLL)/'
    save_path = os.path.join(path, figure_name)

def load_binary(file_path, file_name, results):
    """load data from binary files (.npy)"""
    file = os.path.join(file_path, file_name)
    with open(file,'rb') as f:
        data_array = np.load(f)
    if results == 'h':
        return data_array[:,0]
    elif results == 'psi':
    	return data_array[:,1]

def Li_norm(array1,array2):
	"""compute the L_infity norm between two numpy arrays"""
	return np.max(np.abs(array1-array2))

def L2_norm(array1,array2):
	"""compute the L_2 norm between two numpy arrays"""
	diff = (array1-array2)**2
	return np.sqrt(np.sum(diff))

# get t from the energy file
energy_file = os.path.join(data_path,'energy.csv')
with open(energy_file,'r') as e_f:
    t_steps_full = np.loadtxt(e_f, usecols=0)
print(t_steps_full.shape)

if one_point:
	t_plot = [4.3] # change
else:
	t_plot = t_steps_full[::20] # change

plt.figure(num=1,figsize=(9,7))

for t in t_plot:
	tt   = format(t,'.4f')
	fname = tt+'.npy'
	u  = load_binary(data_path,fname,results)
	u1 = load_binary(data_path1,fname,results)
	u2 = load_binary(data_path2,fname,results)
	u3 = load_binary(data_path3,fname,results)
	u4 = load_binary(data_path4,fname,results)
	u5 = load_binary(data_path5,fname,results)

	L2 = np.array([norm(u1-u), norm(u2-u), norm(u3-u), norm(u4-u), norm(u5-u)])
	#L2 = np.array([L2_norm(h1,h), L2_norm(h2,h), L2_norm(h3,h), L2_norm(h4,h), L2_norm(h5,h)])
	Linf = np.array([Li_norm(u1,u), Li_norm(u2,u), Li_norm(u3,u), Li_norm(u4,u), Li_norm(u5,u)])
	
	if one_point:
		col = 'blue'
	else:
		col = (np.random.random(), np.random.random(), np.random.random()) #random color
	
	plt.loglog(dx,L2,  color=col, marker='^',label=r'$L^2$'+f' (t={t:.4f})')
	plt.loglog(dx,Linf,color=col, marker='o',ls='--',label=r'$L^{\infty}$')


ref = [ele**2 for ele in dx]
plt.loglog(dx,ref,'r-.',lw='2',label='$(\Delta x)^2$')
if results == 'h':
	plt.title(r'Spacial convergence analysis based on $h(x_i,t^n)$', fontsize=16)
elif results == 'psi':
	plt.title(r'Spacial convergence analysis based on $\psi(x_i,t^n)$', fontsize=16)
plt.xlabel(r'$\Delta x$',fontsize=14)
plt.ylabel(r'$\mathcal{E}$',fontsize=14)
if one_point:
	plt.legend(ncols=1, fontsize=10)
else:
	plt.legend(ncols=3, fontsize=10)
plt.grid()
plt.tight_layout()

if save_figure:
    plt.savefig(save_path, dpi=300)
else:
    plt.show()






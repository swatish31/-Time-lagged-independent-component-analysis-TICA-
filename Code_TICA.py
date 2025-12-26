import mdtraj as md
import pyemma
import matplotlib.pyplot as plt
import numpy as np
# ✅ Patch NumPy deprecated alias
if not hasattr(np, 'bool'):
    np.bool = bool
import pyemma
import mdtraj
import types

# ✅ Monkey patch mdtraj to add the missing version attribute
if not hasattr(mdtraj, 'version'):
    mdtraj.version = types.SimpleNamespace(version='1.9.9')
elif not hasattr(mdtraj.version, 'version'):
    mdtraj.version.version = '1.9.9'
feat = pyemma.coordinates.featurizer(r'/home/swati/TICA/KRAS_ALLO/md_C109.gro')
feat.add_backbone_torsions(cossin=True) 

data2 = pyemma.coordinates.load([r'/home/swati/TICA/KRAS_ALLO/md_C109.xtc'], features=feat)

tica = pyemma.coordinates.tica(data2, lag=10, dim=2, kinetic_map=True)
tica_output = tica.get_output()[0]
np.savetxt('tica_output_data2_ALLO_C109.txt', tica_output, fmt='%.6f', delimiter='\t')

plt.scatter(tica_output[:,0], tica_output[:,1], c=range(len(tica_output)), cmap='viridis', s=5)
plt.xlabel('TICA 1')
plt.ylabel('TICA 2')
plt.title('TICA Projection of MD Trajectory')
plt.colorbar(label='Frame index')
plt.show()                









merged file code-------- 


import numpy as np
import matplotlib.pyplot as plt

files = [ r'/home/swati/TICA/KRAS_ALLO/tica_output_data1_ALLO_7599.txt',
    r'/home/swati/TICA/KRAS_ALLO/tica_output_data2_ALLO_C109.txt',
    r'/home/swati/TICA/KRAS_ALLO/tica_output_data2_ALLO_C109.txt',
    r'/home/swati/TICA/KRAS_ALLO/tica_output_data4_ALLO_L150.txt',
    r'/home/swati/TICA/KRAS_ALLO/tica_output_data5_ALLO_V016.txt']

compound_labels = ['7599-1863', 'C109-1028', 'K284-5624', 'L150-1140', 'V016-998']
colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis']

plt.figure(figsize=(8,6))

for idx, file in enumerate(files):
    data = np.loadtxt(file)
    # color by frame index per compound, with different colormaps
    plt.scatter(data[:,0], data[:,1], c=range(len(data)), cmap=colormaps[idx], s=5, label=compound_labels[idx])

plt.xlabel('TICA 1')
plt.ylabel('TICA 2')
plt.title('Merged TICA Projection ')
plt.legend()
plt.colorbar(label='Frame index (per compound)')
plt.show()
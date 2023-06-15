import h5py
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load .mat file
# For part a use 'data/points2D_Set1.mat'
file = h5py.File('data/points2D_Set2.mat', 'r')

# Plot to show how points are scattered
X=file['x']
Y=file['y']
plt.scatter(X,Y)
plt.show()
import matplotlib.pyplot as plt
import numpy as np


fig,z= plt.subplots()
x = np.arange(-7, 7, 0.01)
A = 3
omega = 1
B = 2
y = A * np.sin(omega * x) + B 
z.plot(x, y) 
plt.show() 

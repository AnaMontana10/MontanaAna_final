import numpy as np
import matplotlib.pyplot as plt 


datos = np.genfromtxt("final15.dat")

tiempo = datos[:,0]
x = datos[:,1]
y = datos[:,2]


plt.figure()
plt.plot(x,y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("MontanaAna_final_15.pdf")
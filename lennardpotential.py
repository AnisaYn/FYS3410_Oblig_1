from math import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import*

def lj(r, epsilon=1.0, sigma = 1.5):
    if r > 0.0:
        return epsilon*(sigma**12/r**12-sigma**6/r**6)
    else:
        return None
x = np.arange(0.5, 3.5, 0.001)
vlj = np.vectorize(lj)
fig, ax = plt.subplots()
ax.plot(x,vlj(x),"y-",linewidth=3, label='Lennard-Jones Potential')
plt.axhline(y=0.0, xmin=0.01, xmax=2.0, linewidth=1, color = 'k')
plt.axvline(x=1.0, ymin=0.01, ymax = 1.0, linewidth=1, color='k')

def F(r, epsilon=1.0, sigma = 1.0):
    if r > 0.0:
        return ((24.0*epsilon)/sigma)*(2*(sigma**13/r**13)-(sigma**7/r**7))
    else:
        return None

F = np.vectorize(F)

ax.plot(x,F(x),"r--",linewidth=3, label='Force')
grid(True)
xlim(0.7, 3.3)
ylim(-2.5, 2)
title('Lennard-Jones potential', fontsize=20)
xlabel(r"$r$", fontsize=20)
ylabel(r"$U_{(r)} $ or $F$",fontsize=20)
# Now add the legend with some customizations.
legend = ax.legend(loc='4', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)
    
ax.annotate('attractive force', xy=(1.6, -0.7), xytext=(2.1, -1.2))#,
            #arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('repulsive force', xy=(0.9, 1.0), xytext=(1.5, 0.5))#,
            #arrowprops=dict(facecolor='black', shrink=0.05))
show()



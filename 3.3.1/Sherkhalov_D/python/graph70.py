import numpy as np
import matplotlib.pyplot as plt

a = '300 & 300 & 300 & 296 & 292 & 248 & 44 & 20 & 12 & 4 & 4 & 4 & 4 & 0 & 0 & 0 & 0'
a = np.asarray(list(map(int, a.split('&'))))
da = 4

b = '1.1 & 2.8 & 4.1 & 4.2 & 4.3 & 4.5 & 4.6 & 4.8 & 4.9 & 5.0 & 5.2 & 5.3 & 5.5 & 5.6 & 5.7 & 5.9 & 6.3'
b = np.asarray(list(map(float, b.split('&'))))
db = 0.1

y = a
dy = da
x = b
dx = db

plt.xlabel(r'$B$, мТл', fontsize=14)
plt.ylabel(r'$I_a$, мкА', fontsize=14)
plt.title(r'$V_a = 70\;В$', fontsize=14)
plt.grid(True)
plt.errorbar(x, y, xerr=dx, yerr=dy, fmt='o', color='black', capsize=3)
plt.plot(x, y, color="firebrick", label=r'$I_a(B)$')

plt.legend(loc='best', fontsize=12)
plt.show()
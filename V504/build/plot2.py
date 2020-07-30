from scipy.optimize import curve_fit
import math 
import matplotlib as mpl
mpl.use('pgf')
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams.update({
'font.family': 'serif',
'text.usetex': True,
'pgf.rcfonts': False,
'pgf.texsystem': 'lualatex',
'pgf.preamble': r'\usepackage{unicode-math}\usepackage{siunitx}',
})
#Um die Schriftart anzupassen




I2 , U = np.genfromtxt('Kennlinie 2.txt',unpack=True,skip_header=1)

I = I2 * 10 ** (-3) 

plt.plot(U, I,'r+', label=r'Messdaten der Kennlinie')
plt.xlabel(r"U / Volt")  
plt.ylabel(r"I / A")
plt.xlim(0,90)
plt.ylim(0.0003, 0.0008)
plt.axhline(y = 0.00074 , xmin = 0.0, xmax = 1,  label=r'$I_S$ = 0.74 mA')
plt.grid()
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Kennlinie2.pdf')
plt.clf()




#is ablesen
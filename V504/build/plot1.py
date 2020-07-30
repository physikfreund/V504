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




I2 , U = np.genfromtxt('Kennlinie 1.txt',unpack=True,skip_header=1)

I = I2 * 10 ** (-3) 

plt.plot(U, I,'r+', label=r'Messdaten der Kennlinie')
plt.xlabel(r"U / Volt")  
plt.ylabel(r"I / A")
plt.xlim(0,105)
plt.ylim(0.0001,0.00015)
plt.axhline(y = 0.000145 , xmin = 0.0, xmax = 1,  label=r'$I_S$ = 0.145mA')
plt.grid()
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Kennlinie1.pdf')
plt.clf()




#is ablesen
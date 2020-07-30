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




I2 , U = np.genfromtxt('Kennlinie 3.txt',unpack=True,skip_header=1)

I = I2 * 10 ** (-9) 

Ukorr = U - 1000000*I

def exp(Ukorr, a, b):
    return a*np.exp(-b*Ukorr)


params, covariance_matrix = curve_fit(exp, Ukorr, I)
uncertainties = np.sqrt(np.diag(covariance_matrix))
plt.plot(U, exp(U, *params), "--" , label=r'Fit')
plt.plot(U, I,'r+', label=r'Messdaten der Kennlinie')
plt.xlabel(r"U / Volt")  
plt.ylabel(r"I / A")
plt.xlim(0,1.1)
plt.grid()
plt.tight_layout()
plt.legend(loc="best")





plt.savefig('Kennlinie3.pdf')
plt.clf()

print(params   )
print(uncertainties)


T = (1.602*10**(-19) ) /( 3.08646993 * (1.380*10**(-23)))
tuncert = (8.94283227*10**(-2) /3.08646993) 

print(T)
print(tuncert)
#is ablesen
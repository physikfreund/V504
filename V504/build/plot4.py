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




I2 , U = np.genfromtxt('Kennlinie 4.txt',unpack=True,skip_header=1)
j2 , V = np.genfromtxt('Kennlinie 4b.txt',unpack=True,skip_header=1)

I = I2 * 10 ** (-3) 
j = j2 * 10 ** (-3)

def langmuir(V, a, b):
    return   (1/a**2)* V**b * 0.000233277

params, covariance_matrix = curve_fit(langmuir, V, j)
uncertainties = np.sqrt(np.diag(covariance_matrix))
plt.plot(V, langmuir(V, *params), "--" , label=r'Fit im Raumladungsgebiet')


plt.plot(U, I,'r+', label=r'Messdaten der Kennlinie')
plt.xlabel(r"U / Volt")  
plt.ylabel(r"I / A")
plt.xlim(-5,255)
plt.grid()
plt.axhline(y = 0.0024 , xmin = 0.0, xmax = 1,  label=r'$I_S$ = 2.4 mA')
plt.tight_layout()
plt.legend(loc="best")
plt.savefig('Kennlinie4.pdf')
plt.clf()

print(params)



#is ablesen
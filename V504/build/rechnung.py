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

T = 2048
I = 0.000145

e = 1.602*10**(-19)
k = 1.38*10**(-23)
h = 1.602*10**(-34)
m = 9.109*10**(-31)


a = (-k*T/e) * np.log((I*h**3*T**2)/(4*3.1416*e*m*k**2))

print(a)
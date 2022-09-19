import numpy as np
import matplotlib.pyplot as plt
import latex
from IPython.display import Latex
import math
import mpl_toolkits.axisartist as axisartist
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
x = np.array([4.84,5.03,5.23,5.43,5.62,5.81,6.0,6.21,6.40])
x1 = np.array([5.62,5.81,6.0,6.21,6.40])
x2 = np.array([5.60,5.79,5.98,6.19,6.38])
bins = np.linspace(5.60,6.8, 5)
#print(bins)
bins = bins +0.1
y1,y2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_fa.txt',unpack=True)
z1,z2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_fb.txt',unpack=True)
t1,t2 =np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_overlap_f.txt',unpack=True)
LOS = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\LOS_a.txt',unpack=True)
LOS2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\LOS_b.txt',unpack=True)
fig, ax = plt.subplots(2,1, sharex=True,figsize=(9,5), gridspec_kw={'height_ratios': [1,3]} )
plt.xlabel('redshift', fontsize='x-large')
plt.ylim(0,1)
plt.xlim(4.7,6.5)
ax[1].set_ylabel ('$x_{HI}$',fontsize='x-large')

ax[1].errorbar(x,y1,yerr = y2, uplims=y2,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ", label= r'Ly$\alpha$')
ax[1].errorbar(x,y1,yerr = y2, lolims=False,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ")
ax[1].plot(x, y1+y2, marker='_', color = 'blue',alpha = 0.4, linestyle= '')


ax[1].errorbar(x1,z1,yerr =z2, uplims = z2,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ", label= r'Ly$\beta$')
ax[1].errorbar(x1,z1,yerr =z2, lolims = False,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ")
ax[1].plot(x1, z1+z2, marker='_', color = 'cyan',alpha = 0.4, linestyle= '')

ax[1].errorbar(x2, t1, yerr = t2, xerr = 0.095, uplims = True, color = 'magenta', marker = 'o', linestyle= '', label= r'Ly$\alpha$+Ly$\beta$')
ax[1].errorbar(x2, t1, yerr = t2, xerr = 0.095,  lolims = False, color = 'magenta', linestyle = '')
ax[1].plot(x2, t1+t2, marker='_', color = 'magenta', linestyle= '')
ax[1].plot(x2,t1+t2, marker='_',  color = 'magenta', linestyle= '')
ax[1].plot(x2-0.095, t1, marker='|', color = 'magenta', linestyle= '')
ax[1].plot(x2+0.095,t1, marker='|', color = 'magenta', linestyle= '')



ax[1].legend(loc = 'upper left' )
ax[1].minorticks_on()
ax[1].tick_params(which='both',direction='in',top=True,right=True,labelsize=12)
plt.tight_layout()
ax[0].plot(x, ((LOS)),color= 'blue', marker = '*', linestyle= " ", label = '$N_{LOS}$')
ax[0].plot(x1, ((LOS2)),color= 'magenta', marker = 'o', linestyle= " ", label = '$N_{LOS overlap}$')
ax[0].set_yticks([3,10,20,30,40])
ax[0].set_ylim(0,40)
#ax[0].minorticks_on()
ax[0].tick_params(which='both',direction='in',top=True,right=True,labelsize=12)
#ax[0].set_yscale('log')
ax[0].set_ylabel ('$N_{LOS}$')
fig.suptitle('')
plt.savefig(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\300_n=2-negative flux.png', pad_inches=0.05)
#plt.show()


x = np.array([4.84,5.03,5.23,5.43,5.62,5.81,6.0,6.21,6.40])
x1 = np.array([5.62,5.81,6.0,6.21,6.40])
x2 = np.array([5.60,5.79,5.98,6.19,6.38])
bins = np.linspace(4.7,6.3, 9)
#print(bins)
bins = bins +0.1
y1,y2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_na.txt',unpack=True)
z1,z2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_nb.txt',unpack=True)
t1,t2 =np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\error_overlap_n.txt',unpack=True)
LOS = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\LOS_a.txt',unpack=True)
LOS2 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\LOS_b.txt',unpack=True)
fig, ax = plt.subplots(2,1, sharex=True,figsize=(9,5), gridspec_kw={'height_ratios': [1,3]} )
plt.xlabel('redshift')
plt.ylim(0,1)
plt.xlim(4.7,6.5)
ax[1].set_ylabel ('$x_{HI}$',fontsize='x-large')

ax[1].errorbar(x,y1,yerr = y2, uplims=y2,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ", label= r'Ly$\alpha$')
ax[1].errorbar(x,y1,yerr = y2, lolims=False,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ")
ax[1].plot(x, y1+y2, marker='_', color = 'blue',alpha = 0.4, linestyle= '')


ax[1].errorbar(x1,z1,yerr =z2, uplims = z2,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ", label= r'Ly$\beta$')
ax[1].errorbar(x1,z1,yerr =z2, lolims = False,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ")
ax[1].plot(x1, z1+z2, marker='_', color = 'cyan',alpha = 0.4, linestyle= '')

ax[1].errorbar(x2, t1, yerr = t2, xerr = 0.095, uplims = True, color = 'magenta', marker = 'o', linestyle= '', label= r'Ly$\alpha$+Ly$\beta$')
ax[1].errorbar(x2, t1, yerr = t2, xerr = 0.095, lolims = False, color = 'magenta', linestyle = '')
ax[1].plot(x2, t1+t2, marker='_', color = 'magenta', linestyle= '')
ax[1].plot(x2,t1+t2, marker='_', color = 'magenta', linestyle= '')
ax[1].plot(x2-0.095, t1, marker='|', color = 'magenta', linestyle= '')
ax[1].plot(x2+0.095,t1, marker='|', color = 'magenta', linestyle= '')
ax[1].minorticks_on()
ax[1].tick_params(which='both',direction='in',top=True,right=True,labelsize=12)
plt.tight_layout()
##ax[1].errorbar(x,y1,yerr = y2, uplims=y2,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ", label= r'Ly$\alpha$')
##ax[1].errorbar(x,y1,yerr = y2, lolims=False,color = 'blue', alpha = 0.4 , marker ='x', linestyle = " ")
##ax[1].plot(x, y1+y2, marker='_', color = 'blue',alpha = 0.4, linestyle= '')
##
##
##ax[1].errorbar(x1,z1,yerr =z2, uplims = z2,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ", label= r'Ly$\beta$')
##ax[1].errorbar(x1,z1,yerr =z2, lolims = False,  color= 'cyan',alpha = 0.4, marker = 's', linestyle= " ")
##ax[1].plot(x1, z1+z2, marker='_', color = 'cyan',alpha = 0.4, linestyle= '')
##
##ax[1].errorbar(x2, t1, yerr = t2, xerr = 0.1, uplims = True, color = 'magenta', marker = 'o', linestyle= '', label= r'Ly$\alpha$+Ly$\beta$')
##ax[1].errorbar(x2, t1, yerr = t2,  lolims = False, color = 'magenta', linestyle = '')
##ax[1].plot(x2, t1+t2, marker='_', color = 'magenta', linestyle= '')
##ax[1].plot(x2,t1+t2, marker='_', color = 'magenta', linestyle= '')
##ax[1].plot(x2-0.1, t1, marker='|', color = 'magenta', linestyle= '')
##ax[1].plot(x2+0.1,t1, marker='|', color = 'magenta', linestyle= '')

ax[1].legend(loc = 'upper left' )
ax[0].plot(x,(LOS),color= 'blue', marker = '*', linestyle= " ", label = '$N_{LOS}$')
ax[0].plot(x1,(LOS2),color= 'magenta', marker = 'o', linestyle= " ", label = '$N_{LOS overlap}$')
ax[0].set_yticks([3,10,20,30,40])
ax[0].set_ylim(0,40)
ax[0].set_ylabel ('$N_{LOS}$', fontsize='x-large')
ax[0].tick_params(which='both',direction='in',top=True,right=True,labelsize=12)
fig.suptitle('')
plt.savefig(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\300_n=2-thrashold.png')
#plt.show()

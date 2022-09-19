import numpy as np
import math as mt
import matplotlib
import scipy
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
la = 1215.6701 #Lya wavelength rest frame 
lb = 1025.7223 #Lyb wavelength rest frame 

#Import the data for each object
z_emi, z_max, z1, zmina, z1b, zminb = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', usecols=(1, 2, 3, 4, 5, 6), unpack=True)
#Import the name of the objects
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', dtype='str', usecols=(0))

#Functions that uses the minimum and maximum redshift to set the extremes for the Lya and Lyb forest in wavelength 
def z2la(z):
    l=(z+1)*la
    return l
def z2lb(z):
    l=(z+1)*lb
    return l


pixel= []
#Iteration for each object
for i in range(0,len(name)):
    l_max = z2la(z_max[i])
    l_min = z2la(zmina[i])
    #Import data relative to each object: mean wavelength of the pixel (a1), extremes of the pixel in wavelength (a2,a3), flux (a4), associated error(a5)
    a1,a2,a3,a4,a5 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\new_spectra\clean\{}_VIS_spec_clean.txt'.format(name[i]), unpack= True)
    #flux [10**-19 erg/s/cm^2/A]
    a4 = a4*10**19
    a5 = a5*10**19    
    for j in range(0,len(a1)):
        #Condition for dark pixel
         if (a4[j]) < 2* a5[j]:
             #Collect the dark pixels in a list
              pixel.append(a4[j])
    #Take the mean and the standard deviation
    a = np.mean(pixel)
    b = np.std(pixel)
    #Make the histograms
    plt.figure()
    plt.hist(pixel, 10 ,density=False, facecolor='blue', alpha=0.7)
    plt.axvline(x=0, ymin=0, ymax=200, color="k", linestyle="dotted")
    plt.axvline(x=a, ymin=0, ymax=200, color="y", linestyle="-.", label='mean flux, $\mu$={:.03f}'.format(a))
    plt.axvspan(a-b,a+b,facecolor='grey',alpha=0.6, label= r'1$\sigma$={:.03f}'.format(b))
    #plt.title(r'{}'.format(name[i]))
    plt.xlabel('flux [10**-19 erg/s/cm^2/A]')
    plt.ylabel('pixel')
    plt.legend(loc='upper left')
    #Save the images
    plt.savefig(r"C:\Users\UTENTE\Desktop\Final analysis\new_spectra\hist_2s\{}-Lya.png".format(name[i]))
    #plt.show()
    #Format the cycle 
    pixel *=0
    













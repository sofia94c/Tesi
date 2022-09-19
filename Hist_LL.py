import numpy as np
import math as mt
import matplotlib
import scipy
from scipy import stats
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
from scipy.stats import norm
from astropy.modeling import models, fitting
#Import the data for each object
z_emi, z_max, z1, zmina, z1b, zminb = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', usecols=(1, 2, 3, 4, 5, 6), unpack=True)
#Import the name of the objects
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', dtype='str', usecols=(0))

la = 1215.6701 #Lya wavelength rest frame 
lb = 1025.7223 #Lyb wavelength rest frame 
lLL=912 #Lyman Limit (LL) wavelength rest frame
#Function useful to set the starting point for the pixel count
def z2lambda (z,lamb):
    l = (z+1)*lamb
    return l
pixel= []
err=[]
#Iteration for each object
for i in range(0, len(name)):
    #Take the wavelength below the LL of each spectra
    L_ll = z2lambda(z_max[i],lLL)
    #Import data relative to each object: mean wavelength of the pixel (a1), extremes of the pixel in wavelength (a2,a3), flux (a4), associated error(a5)
    a1,a2,a3,a4,a5 = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\spec_clean\{}_VIS_rebinned_spec.txt'.format(name[i]), unpack= True)
    #From nm to Angstrom
    a1=a1*10
    #flux [10**-19 erg/s/cm^2/A]
    a4 = a4*10**19
    a5 = a5*10**19
    #print(L_ll)
    #Select the pixel in the interval of interest
    for j in range (0, len(a1)):
        if a1[j]>L_ll-400 and a1[j]<L_ll:
            #Collect the pixels in a list
            pixel.append(a4[j])
            err.append(a5[j])
    #Take the mean and the standard deviation
    a = np.mean(pixel)
    b = np.std(pixel)
    c = np.mean(err)
    print(c)
    #Make the histograms
    plt.figure()
    plt.hist(pixel,10,density=False, facecolor='Green', alpha=0.7)#,label='flux')
    plt.axvline(x=0, ymin=0, ymax=200, color="black", linestyle="dotted")
    plt.axvline(x=a, ymin=0, ymax=200, color="yellow", linestyle="-.", label=r'mean flux, $\mu$ ={:.03f}'.format(a))
    plt.axvspan(a-b,a+b,facecolor='grey',alpha=0.5, label= r'1$\sigma$={:.03f}'.format(b))
    #plt.title('{}'.format(name[i]))
    plt.xlabel('flux [10**-19 erg/s/cm^2/A]')
    plt.ylabel('pixel')
    plt.legend(loc='best')
    #Save the images
    plt.savefig(r"C:\Users\UTENTE\Desktop\Final analysis\new_spectra\LL\{}_LL.png".format(name[i]))
    #plt.show()
    #Format the cycle 
    pixel*=0


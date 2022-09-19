import numpy as np
#Import the data for each object
z_emi, z_max, z1_a, z2_a, z1_b, z2_b = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', usecols=(1, 2, 3, 4, 5, 6), unpack=True)
#Import the name of the objects
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', dtype='str', usecols=(0))

la = 1215.6701 #Lya wavelength rest frame 
lb = 1025.7223 #Lyb wavelength rest frame

# lambdas in Angstrom given z_min=z2 and z_max=z1
def z_lamb_min(z2):
    l_min_a = (z2+1)*la
    return l_min_a

def z_lamb_max(z1):
    l_max_a = (z1+1)*la
    return l_max_a

# 1D array for lmin and lmax given each z_min, z_max
L_a_min = np.zeros(len(z_max))
L_a_max = np.zeros(len(z_max))
#Compute the lambda minimum and maximum for each redshift
for i in range(0, len(z_max)):
    L_a_min[i] = z_lamb_min(z2_a[i])
    L_a_max[i] = z_lamb_max(z_max[i])
    
#Check function to control if the pixel considered in within the Lya wavelength range 
def check_range(X, X_m, X_M, Y, dY, lym_min, lym_max):
    for i in range(0, len(x)):
        if x[i]<=lym_max and x[i]>=lym_min:
            X.append(x[i])
            X_m.append(xmin[i])
            X_M.append(xmax[i])
            Y.append(y[i])
            dY.append(dy[i])
        else:
            continue


# Generalized cleaning + save
for i in range(0, len(name)):
    #Import data relative to each object: mean wavelength of the pixel (x), extremes of the pixel in wavelength (xmin,xmax), flux (y), associated error(dy) for the objects with DLAs within the Lya forest
    x, xmin, xmax, y, dy = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec.txt'.format(name[i]), unpack=True)
    x = x*10
    xmin = xmin*10
    xmax = xmax*10
    X = []
    X_m = []
    X_M = []
    Y = []
    dY = []    
    check_range(X, X_m, X_M, Y, dY, L_a_min[i], L_a_max[i])
    data = np.column_stack((X, X_m, X_M, Y, dY))
    np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]), data, delimiter='\t', fmt='%.6f\t%.6f\t%.6f\t%.7e\t%.7e')
    X *= 0
    X_m *= 0
    X_M *= 0
    Y *= 0
    dY *= 0
    x *= 0
    xmin *= 0
    xmax *= 0
    y *= 0
    dy *= 0
    i = i+1


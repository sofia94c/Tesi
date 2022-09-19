import numpy as np
z_emi, z_max, z2_a,z2_b, x_n = np.loadtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_100kms^-1\dist_z.txt', usecols=(1, 2, 3, 4, 5), unpack=True)
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_100kms^-1\dist_z.txt', dtype='str', usecols=(0))
la= 1215.6701
def convert(x):
     z = (x/la)-1
     return z
for i in range(0, len(name)):
     x, xmin, xmax, y, dy = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]), unpack=True)
     Y_n=np.zeros(len(x),  dtype=float)
     dY_n=np.zeros(len(x),  dtype=float)
     X = np.zeros(len(x),  dtype=float)
     #x = x*10
     aux = 10000.
     index = 0
     
     for j in range (0, len(x)):
          var = x[j]-x_n[i]
          var = np.abs(var)
          if var < aux:
               aux = var
               index = j
          
##         if var >0 and var < 1:
##             print('0')
##         elif var <0 and var > -1:
##             print('1')
     Y = y[index]
     print(Y)
     print(x[index])
     print(x_n[i])

     for k in range (0,len(x)):
          Y_n[k]=(y[k]/Y)
          dY_n[k]=(dy[k]/Y)
          X[k] = convert(x[k])
 
             #print('1')
     data = np.column_stack((X, xmin, xmax, Y_n, dY_n))
     np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_norm.txt'.format(name[i]), data, fmt='%.6f\t%.6f\t%.6f\t%.7e\t%.7e', delimiter='\t')
                     
     
     Y_n *= 0
     dY_n *= 0
     x *= 0
     xmin *= 0
     xmax *= 0
     y *= 0








import numpy as np
import statistics
z_max = 6.5
z_min = 4.7
la = 1215.6701
lb = 1025.7223

#Create an array for z
z_mM = np.linspace(z_max, z_min, 10)
#Import the name of the objects
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', dtype='str', usecols=(0))

#Conversion from wavelength to redshift
def convert_z(x):
    z = ((x)/la)-1
    return z

def convert_zb(xb):
    zb = ((xb)/lb)-1
    return zb
#Check function for z
def is_inrange(z, zupp, zlow):
    if z>zlow and z<=zupp:
        return 1
    else:
        return 0


        
''' case 1: in 6.5-6.3
    case 10: in 4.9-4.7
'''
#Adopt threshold 
n=2
#Function for the dark pixel count with threshold and negative method
def single_count(z, cnt, y, cnt3, dy, cnt4, sumz1, sumz2):
    # case 1
    if is_inrange(z, 6.5, 6.3):
        cnt[0] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[0]+=1
            sumz1[0] +=z
        if abs(y)< n * dy:
            cnt4[0]+=1
            sumz2[0] +=z
    # case 2
    if is_inrange(z, 6.3, 6.1):
        cnt[1] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[1]+=1
            sumz1[1]+=z
        if abs(y)< n * dy:
            cnt4[1]+=1
            sumz2[1]+=z
    if is_inrange(z, 6.1, 5.9):
        cnt[2] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[2]+=1
            sumz1[2]+=z
        if abs(y)< n * dy:
            cnt4[2]+=1
            sumz2[2]+=z
    if is_inrange(z, 5.9, 5.7):
        cnt[3] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[3]+=1
            sumz1[3]+=z
        if abs(y)< n * dy:
            cnt4[3]+=1
            sumz2[3]+=z
    if is_inrange(z, 5.7, 5.5):
        cnt[4] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[4]+=1
            sumz1[4]+=z
        if abs(y)< n * dy:
            cnt4[4]+=1
            sumz2[4]+=z
    if is_inrange(z, 5.5, 5.3):
        cnt[5] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[5]+=1
            sumz1[5]+=z
        if abs(y)< n * dy:
            cnt4[5]+=1
            sumz2[5]+=z
    if is_inrange(z, 5.3, 5.1):
        cnt[6] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[6]+=1
            sumz1[6]+=z
        if abs(y)< n * dy:
            cnt4[6]+=1
            sumz2[6]+=z
    if is_inrange(z, 5.1, 4.9):
        cnt[7] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[7]+=1
            sumz1[7]+=z
        if abs(y)< n * dy:
            cnt4[7]+=1
            sumz2[7]+=z
    if is_inrange(z, 4.9, 4.7):
        cnt[8] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[8]+=1
            sumz1[8]+=z
        if abs(y)< n * dy:
            cnt4[8]+=1
            sumz2[8]+=z
    if is_inrange(z, 4.7, 4.5):
        cnt[9] += 1
        if y<0 and abs(y)<n*dy:
        #if y<0:
            cnt3[9]+=1
            sumz1[9]+=z
        if abs(y)< n * dy:
            cnt4[9]+=1
            sumz2[9]+=z


#Count the contributing LOS
def check_count(cnt, ref):
    if cnt!=0 and cnt > ref:
        return 1
    else:
        return 0



# Generalizing for all the objects
i = 0
k = 0
z_max = 6.5
z_min = 4.7
z_mM = np.linspace(z_max, z_min, 10)
cnt = np.zeros(len(z_mM)-1, dtype='int')
cnt2 = np.zeros(len(cnt), dtype='int')
cnt3 = np.zeros(len(cnt), dtype='int')
cnt4 = np.zeros(len(cnt), dtype='int')
sumz1 = np.zeros(len(cnt), dtype='float')
sumz2 = np.zeros(len(cnt), dtype='float')
#Dark pixel count in Lya forest
for i in range(0,len(name)):
#Import data relative to each object: mean wavelength of the pixel (x), extremes of the pixel in wavelength (xmin,xmax), flux (y), associated error(dy) for the objects with DLAs within the Lya forest
    x, xmin, xmax, y, dy = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]), unpack=True)
    Z1=convert_z(x)
    Zmin1=convert_z(xmin)
    Zmax1=convert_z(xmax)
    cnt_check= cnt.copy()
    #Count the dark pixels
    for j in range(0, len(Z1)):
            single_count(Z1[j], cnt, y[j], cnt3, dy[j], cnt4, sumz1, sumz2)
            j += 1        
    #Count the contributing LOS for each redshift bin        
    for k in range(0, len(cnt)):
        tot = check_count(cnt[k], cnt_check[k])
        cnt2[k]+= tot
        
    #Clean    
    x *= 0
    xmin *= 0
    xmax *= 0
    y *= 0
    dy *= 0
    Z1 *= 0
    Zmin1 *= 0
    Zmax1 *= 0
    i = i+1
print('z mean 1:',sumz1/cnt3)
print('z mean 2:',sumz2/cnt4)

cnt=cnt[::-1]
cnt2=cnt2[::-1]
cnt3=cnt3[::-1]
cnt4=cnt4[::-1]

print('pixel number:',cnt)
print('f',cnt3)
print('n',cnt4)
print('QSO number:',cnt2)
#print('flux<0 number',(cnt3*2))
print('flux<0 fraction number',(cnt3*2)/cnt)
#print('f<n*df number',cnt4)
print('f<n*df fraction number',cnt4/cnt)
#Jackknife statistics to derive the mean and variance from the fractions calculated during each resampling
cnt3_aux = np.zeros((len(name),9))
cnt4_aux = np.zeros((len(name),9))
w = []
for t in range(len(name)):
    w.append(t)
for t in range(len(name)):
    aux = w.copy()
    aux.pop(t)
    cnt = np.zeros(len(z_mM)-1, dtype='int')
    cnt2 = np.zeros(len(cnt), dtype='int')
    cnt3 = np.zeros(len(cnt), dtype='int')
    cnt4 = np.zeros(len(cnt), dtype='int')
    sumz1 = np.zeros(len(cnt), dtype='float')
    sumz2 = np.zeros(len(cnt), dtype='float')
    
    for i in aux:
        x, xmin, xmax, y, dy = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]),  unpack=True)
        
        Z1=convert_z(x)
        Zmin1=convert_z(xmin)
        Zmax1=convert_z(xmax)
        cnt_check= cnt.copy()
        for j in range(0, len(Z1)):
            single_count(Z1[j], cnt, y[j], cnt3, dy[j], cnt4, sumz1, sumz2)
            j += 1   
            
            
            
        for k in range(0, len(cnt)):
            tot = check_count(cnt[k], cnt_check[k])
            cnt2[k]+= tot
    
     

            
        x *= 0
        xmin *= 0
        xmax *= 0
        y *= 0
        dy *= 0
        Z1 *= 0
        Zmin1 *= 0
        Zmax1 *= 0

    cnt=cnt[::-1]
    cnt2=cnt2[::-1]
    cnt3=cnt3[::-1]
    cnt4=cnt4[::-1]
    for m in range(9):
        cnt3_aux[t,m] = 2*cnt3[m]/cnt[m]
    for m in range(9):
        cnt4_aux[t,m] = cnt4[m]/cnt[m]
#Save the data
np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\negative_flux.txt', cnt3_aux, delimiter='\t', fmt='%.4f')
np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\threshold.txt', cnt4_aux, delimiter='\t', fmt='%.4f')
##

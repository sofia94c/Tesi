import numpy as np

z_max = 6.50
z_min = 5.45
la = 1215.6701
lb = 1025.7223
#Import the name of the objects
name = np.genfromtxt(r'C:\Users\UTENTE\Desktop\Final analysis\ANALYSIS WITHOUT BAL_300kms^-1\distanza tra due z.txt', dtype='str', usecols=(0))
#Conversion from wavelength to redshift
def convert_z(x):
    za = ((x)/la)-1
    return za

def convert_zb(x):
    zb = ((x)/lb)-1
    return zb
#Check function for z
def is_inrange(z, zupp, zlow):
    if z>zlow and z<=zupp:
        return 1
    else:
        return 0

#Adopt threshold 
n=2

#Function for the dark pixel count with threshold and negative method
def single_count(za, zb,xM, xm, cnt, ya, yb, dya, dyb, cnt3, cnt4,sum1):
    #Overlapping condition
    if za==zb:
        z=zb
    if (np.abs((zb-za)))<= ((xM-xm)/2):
        za = zb
        z = zb
     # case 1   
        if is_inrange(z, 6.50, 6.30):
            cnt[0] += 1
            if ya<0 and yb<0 and abs(ya)<n*dya and abs(yb)<n*dyb:
            #if ya<0 and yb<0:
                cnt3[0]+=1
                sum1[0]+=z
            if abs(ya)< n * dya and abs(yb)< n * dyb:
                cnt4[0]+=1
    # case 2
        if is_inrange(z, 6.30, 6.10):
            cnt[1] += 1
            if ya<0 and yb<0 and abs(ya)<n*dya and abs(yb)<n*dyb:
            #if ya<0 and yb<0:
                cnt3[1]+=1
                sum1[1]+=z
            if abs(ya)< n * dya and abs(yb)< n * dyb:
                    cnt4[1]+=1
        if is_inrange(z, 6.10, 5.90):
            cnt[2] += 1
            if ya<0 and yb<0 and abs(ya)<n*dya and abs(yb)<n*dyb:
            #if ya<0 and yb<0:
                cnt3[2]+=1
                sum1[2]+=z
            if abs(ya)< n * dya and abs(yb)< n * dyb:
                    cnt4[2]+=1
        if is_inrange(z, 5.90, 5.70):
            cnt[3] += 1
            if ya<0 and yb<0 and abs(ya)<n*dya and abs(yb)<n*dyb:
            #if ya<0 and yb<0:
                cnt3[3]+=1
                sum1[3]+=z
            if abs(ya)< n * dya and  abs(yb)< n * dyb:
                    cnt4[3]+=1
        if is_inrange(z, 5.70, 5.45):
            cnt[4] += 1
            if ya<0 and yb<0 and abs(ya)<n*dya and abs(yb)<n*dyb:
            #if ya<0 and  yb<0:
                cnt3[4]+=1
                sum1[4]+=z
            if abs(ya)< n * dya and abs(yb)< n * dyb:
                cnt4[4]+=1
       
#Count the contributing LOS
def check_count(cnt, ref):
    if cnt!=0 and cnt > ref:
        return 1
    else:
        return 0

# Generalizing for all the objects
i = 0
j = 0
z_mM = np.linspace(z_max, z_min, 6)
cnt = np.zeros(len(z_mM)-1, dtype='int')
cnt2 = np.zeros(len(cnt), dtype='int')
cnt3 = np.zeros(len(cnt), dtype='int')
cnt4 = np.zeros(len(cnt), dtype='int')
sum1 = np.zeros(len(cnt), dtype='float')
ZA=[]
ZMINA=[]
ZMAXA=[]
Ya=[]
dYa=[]
ZB=[]
ZMINB=[]
ZMAXB=[]
Yb=[]
dYb=[]
#Dark pixel count in Lya+Lyb forests
for i in range(len(name)):
    #Import data relative to each object: mean wavelength of the pixel (x), extremes of the pixel in wavelength (xmin,xmax), flux (y), associated error(dy) for the objects with DLAs within the Lya forest
    xa, xmina, xmaxa, ya, dya = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]), unpack=True)
    Za=convert_z(xa)
    ZA=Za.tolist()
    
    Zmina=convert_z(xmina)
    ZMINA=Zmina.tolist()
    
    Zmaxa=convert_z(xmaxa)
    ZMAXA=Zmaxa.tolist()
    
    Ya=ya.tolist()
    dYa=dya.tolist()

    xb, xminb, xmaxb, yb, dyb = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_Lyb.txt'.format(name[i]), unpack=True)
    Zb=convert_zb(xb)
    ZB=Zb.tolist()
    
    Zminb=convert_zb(xminb)
    ZMINB=Zminb.tolist()
    Zmaxb=convert_zb(xmaxb)
    ZMAXB=Zmaxb.tolist()
    Yb=yb.tolist()
    dYb=dyb.tolist()
    cnt_check= cnt.copy()
    #Count the dark pixels
    for w in range(0, len(ZA)):
        for q in range (0, len(ZB)):
            single_count(ZA[w], ZB[q],ZMAXA[w], ZMINA[w], cnt, Ya[w], Yb[q], dYa[w], dYb[q], cnt3, cnt4, sum1)
            q+=1
        w+=1
    #Count the contributing LOS for each redshift bin 
    for k in range(0, len(cnt)):
        tot = check_count(cnt[k], cnt_check[k])
        cnt2[k]+= tot
    #Clean    
    xb *= 0
    xminb *= 0
    xmaxb *= 0
    yb *= 0
    dyb *= 0
    Zb *= 0
    Zminb *= 0
    Zmaxb *= 0
    
    xa *= 0
    xmina *= 0
    xmaxa *= 0
    ya *= 0
    dya *= 0
    Za *= 0
    Zmina *= 0
    Zmaxa *= 0
    i = i+1
print(sum1/cnt3)
cnt=cnt[::-1]
cnt2=cnt2[::-1]
cnt3=cnt3[::-1]
cnt4=cnt4[::-1]
#sumz1=sumz1[::-1]
#semz2=sumz2[::-1]
print('pixel number:',cnt)
print('QSO number:',cnt2)
print('flux<0 number',(cnt3*4)/cnt)
print('f<n*df number',cnt4/cnt) 
print('f',cnt3)
print('n',cnt4)
###Jackknife statistics to derive the mean and variance from the fractions calculated during each resampling
cnt3_aux = np.zeros((len(name),5))
cnt4_aux = np.zeros((len(name),5))


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
    sum1 = np.zeros(len(cnt), dtype='float')
    

    for i in aux:
        xa, xmina, xmaxa, ya, dya = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_clean.txt'.format(name[i]), unpack=True)
        Za=convert_z(xa)
        ZA=Za.tolist()
        Zmina=convert_z(xmina)
        ZMINA=Zmina.tolist()
        Zmaxa=convert_z(xmaxa)
        ZMAXA=Zmaxa.tolist()
        Ya=ya.tolist()
        dYa=dya.tolist()

        xb, xminb, xmaxb, yb, dyb = np.loadtxt(r'C:\Users\UTENTE\Desktop\spec50kms\{}_VIS_rebinned50_spec_Lyb.txt'.format(name[i]), unpack=True)
        Zb=convert_zb(xb)
        ZB=Zb.tolist()
        Zminb=convert_zb(xminb)
        ZMINB=Zminb.tolist()
        Zmaxb=convert_zb(xmaxb)
        ZMAXB=Zmaxb.tolist()
        Yb=yb.tolist()
        dYb=dyb.tolist()
        cnt_check= cnt.copy()
        for s in range(0, len(ZA)):
            for q in range (0, len(ZB)):
                single_count(ZA[s], ZB[q],ZMAXA[s], ZMINA[s], cnt, Ya[s], Yb[q], dYa[s], dYb[q], cnt3, cnt4, sum1)
                q+=1
            s+=1
        for k in range(0, len(cnt)):
            tot = check_count(cnt[k], cnt_check[k])
            cnt2[k]+= tot
           
        xb *= 0
        xminb *= 0
        xmaxb *= 0
        yb *= 0
        dyb *= 0
        Zb *= 0
        Zminb *= 0
        Zmaxb *= 0
        
        xa *= 0
        xmina *= 0
        xmaxa *= 0
        ya *= 0
        dya *= 0
        Za *= 0
        Zmina *= 0
        Zmaxa *= 0
        i = i+1
    
    cnt=cnt[::-1]
    cnt2=cnt2[::-1]
    cnt3=cnt3[::-1]
    cnt4=cnt4[::-1]
    for m in range(5):
        cnt3_aux[t,m] = 4*cnt3[m]/cnt[m]
    for m in range(5):
        cnt4_aux[t,m] = cnt4[m]/cnt[m]

#Save the data
np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\negative_flux_overlap.txt', cnt3_aux, delimiter='\t', fmt='%.4f')
np.savetxt(r'C:\Users\UTENTE\Desktop\spec50kms\threshold_overlap.txt', cnt4_aux, delimiter='\t', fmt='%.4f')



















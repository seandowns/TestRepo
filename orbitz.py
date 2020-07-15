import numpy as np

#Hohmann Transfer to the Munar SOI

muKerb = 3.5316e3 #km^3/s^2
rKerb = 600 #km

muMun = 6.5138398e1 #km^3/s^2
rMun = 200 #km
rSOIMun = 2429.559

MunDist = 12000 # km, Moon is in a circular equatorial orbit around Kerbin

h0 = 100 #km circ orbit to start.
r0 = h0 + rKerb
#wowowow

v0Circ = np.sqrt(muKerb / r0) #initial circular velocity

ra_postTLI = MunDist - rSOIMun

a_transfer = (r0 + ra_postTLI) / 2 #SMA of transfer ellipse

vp_transfer = np.sqrt((2 * muKerb / r0) - (muKerb / a_transfer)) 
va_transfer = np.sqrt((2 * muKerb / ra_postTLI) - (muKerb / a_transfer)) 

v_mun = np.sqrt(muKerb / MunDist)

print(va_transfer)
print(v_mun)
print(vp_transfer - v0Circ)
print(vp_transfer)


#Two segments, meeting on the SOI... position patch points could be parameterized by an angle.
# objective function: dv
# OV's... Time of departure..., time and position of arrival on the sphere of influence (solve Lambert's problem for DV's)
# 

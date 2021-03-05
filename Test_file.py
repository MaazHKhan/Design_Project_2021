import numpy as np
import matplotlib.pyplot as plt
import pylab as lab
from commpy.filters import rrcosfilter


Data = np.genfromtxt("RRC.txt",dtype=lab.complex128)

plt.plot(Data)
plt.show
#FREQ = 99994.3 Hz
#Phase = 88.6
X = 10

Matched_Sync_Freq = 99994.3

t = np.arange(-X, X, 0.5)

Sinc = 5*np.sinc((t*np.pi)/X)
#plt.plot(Sinc)
#plt.show()

Filter_O = np.convolve(Data, Sinc, "Same")

filter_data =Filter_O[3150:27385] 

plt.plot(np.abs(filter_data))
plt.show()



DM = np.savetxt("DM.txt", Filter_O)



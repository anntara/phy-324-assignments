

save=True # if True then we save images as files

import matplotlib.pyplot as plt
import numpy as np
N=100   # N is how many data points we will have in our sine wave
time=np.arange(N)

T=1.0
freq=[]
while T<=N:
    x = 0.09+1/T*10
    freq.append(x)
    T+=1
    
freq=np.array(freq)
print(freq)
wt = 2.0*np.pi*freq


A1=13.   # wave amplitude
#T1=100.  # wave period
y=A1*np.sin(wt*time)

z1=np.fft.fft(y)
#z2=np.fft.fft(x)

fig, (ax1,ax2) = plt.subplots(1,2)
ax1.plot(time/N,y)
ax2.plot(np.abs(z1))
ax1.set_xlabel('Position-Time')
ax2.set_xlabel('Absolute value of FFT of Position-Time\n(Amplitude-Frequency)')
ax1.set_ylim(-20,20)
ax2.set_ylim(0,500)
ax1.set_ylabel('sine wave')
mydpi=300
plt.tight_layout()
if (save): plt.savefig('ex4.png',dpi=mydpi)
plt.show()

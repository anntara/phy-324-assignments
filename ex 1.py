# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:29:04 2020

@author: annta
"""

save=True # if True then we save images as files
from random import gauss
import matplotlib.pyplot as plt
import numpy as np
N=100   # N is how many data points we will have in our sine wave
time=np.arange(N)
#for wave 1
A1=5.   # wave amplitude
T1=13.  # wave period
y1=A1*np.sin(2.*np.pi*time/T1)
noise_amp=A1/2. 
# set the amplitude of the noise relative to sine's amp
#for wave 2
A2=11.   # wave amplitude
T2=7.  # wave period
y2=A2*np.sin(2.*np.pi*time/T2)
noise_amp=A2/2. 

#wave1+wave2
y = y1+y2
"""
i=0
noise=[]
while i < N:
    noise.append(gauss(0,noise_amp))
    i+=1
"""
noise=[gauss(0,noise_amp) for _usused_variable in range(len(y))]

# this line, and the commented block above, do exactly the same thing
#x=y+noise
# y is our pure sine wave, x is y with noise added
z1=np.fft.fft(y)
#z2=np.fft.fft(x)
# take the Fast Fourier Transforms of both x and y
fig, (ax1,ax2) = plt.subplots(1,2)

#fig, ( (ax1,ax2), (ax3,ax4) ) = plt.subplots(2,2,sharex='col',sharey='col')
""" 
this setups up a 2x2 array of graphs, based on the first two arguments
of plt.subplots()
the sharex and sharey force the x- and y-axes to be the same for each 
column
"""
ax1.plot(time/N,y)
ax2.plot(np.abs(z1))
#ax3.plot(time/N,x)
#ax4.plot(np.abs(z2))

""" 
our graphs are now plotted
(ax1,ax2) is a list of figures which are the top row of figures
therefore ax1 is top-left and ax2 is top-right
we plot the position-time graphs rescaled by a factor of N so that
the FFT x-axis agrees with the frequency we could measure from the
position-time graph. by default, both graphs use "data-point number"
on their x-axes, so would go 0 to 200 since N=200.
"""
#fig.subplots_adjust(hspace=0)
# remove the horizontal space between the top and bottom row
ax1.set_xlabel('Position-Time')
ax2.set_xlabel('Absolute value of FFT of Position-Time\n(Amplitude-Frequency)')
ax1.set_ylim(-20,20)
ax2.set_ylim(0,500)
ax1.set_ylabel('wave1 + wave2')

'''
ax3.set_xlabel('Position-Time')
ax4.set_xlabel('Absolute value of FFT of Position-Time\n(Amplitude-Frequency)')
ax3.set_ylim(-13,13)
ax4.set_ylim(0,480)
ax1.set_ylabel('Pure Sine Wave')
ax3.set_ylabel('Same Wave With Noise')
'''
mydpi=300
plt.tight_layout()
if (save): plt.savefig('ex1.png',dpi=mydpi)
plt.show()
"""
plt.show() displays the graph on your computer
plt.savefig will save the graph as a .png file, useful for including
in your report so you don't have to cut-and-paste
"""
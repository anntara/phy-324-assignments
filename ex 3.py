# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:13:07 2020

@author: annta
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:53:25 2017
@author: Brian
"""
save=True # if True then we save images as files
mydpi=300
import pickle
#from random import gauss
import matplotlib.pyplot as plt
import numpy as np

with open('noisy_sine_wave','rb') as file:
    data_from_file=pickle.load(file)
"""
the above few lines makes an array called data_from_file which contains
a noisy sine wave as long as you downloaded the file "noisy_sine_wave" 
and put it in the same directory as this python file

pickle is a Python package which nicely saves data to files. it can be
a little tricky when you save lots of data, but this file only has one
object (an array) saved so it is pretty easy
"""

N=2000   # N is how many data points we will have in our sine wave
time=np.arange(N)
A1=10.   # wave amplitude
T1=100.  # wave period
y=A1*np.sin(2.*np.pi*time/T1)
#noise_amp=A1/2. 
# set the amplitude of the noise relative to sine's amp

#noise=[gauss(0,noise_amp) for _usused_variable in range(len(y))]

x=data_from_file
z1=np.fft.fft(y)
z2=np.fft.fft(x)

M=len(z2)
freq=np.arange(M)  # frequency values, like time is the time values


width1=100  # width=2*sigma**2 where sigma is the standard deviation
peak1= 292   # ideal value is approximately N/T1
filter_function1=(np.exp(-(freq-peak1)**2/width1)+np.exp(-(freq+peak1-M)**2/width1))
width2=100  # width=2*sigma**2 where sigma is the standard deviation
peak2= 150  # ideal value is approximately N/T1
filter_function2=(np.exp(-(freq-peak2)**2/width2)+np.exp(-(freq+peak2-M)**2/width2))
width3=100  # width=2*sigma**2 where sigma is the standard deviation
peak3= 118   # ideal value is approximately N/T1
filter_function3=(np.exp(-(freq-peak3)**2/width3)+np.exp(-(freq+peak3-M)**2/width3))
filter_function=filter_function1+filter_function2+filter_function3

'''
width=200  # width=2*sigma**2 where sigma is the standard deviation
peak= 300   # ideal value is approximately N/T1
filter_function=(np.exp(-(freq-peak)**2/width)+np.exp(-(freq+peak-M)**2/width))
'''
z_filtered=z2**filter_function

"""
we choose Gaussian filter functions, fairly wide, with
one peak per spike in our FFT graph
we eyeballed the FFT graph to figure out decent values of 
peak and width for our filter function
a larger width value is more forgiving if your peak value
is slightly off
making width a smaller value, and fixing the value of peak,
will give us a better final result
"""
fig, (ax1,ax2,ax3)=plt.subplots(3,1,sharex='col')
# this gives us an array of 3 graphs, vertically aligned
ax1.plot(np.abs(z2))  
ax2.plot(np.abs(filter_function))
ax3.plot(np.abs(z_filtered))
"""
note that in general, the fft is a complex function, hence we plot
the absolute value of it. in our case, the fft is real, but the
result is both positive and negative, and the absolute value is still
easier to understand
if we plotted (abs(fft))**2, that would be called the power spectra
"""
fig.subplots_adjust(hspace=0)
ax1.set_ylim(0,10000)
ax2.set_ylim(0,1.2)
ax3.set_ylim(0,550)
ax1.set_ylabel('Noisy FFT')
ax2.set_ylabel('Filter Function')
ax3.set_ylabel('Filtered FFT')
ax3.set_xlabel('Absolute value of FFT of Position-Time\n(Amplitude-Frequency)')
plt.tight_layout() 
""" 
the \n in our xlabel does not save to file well without the
tight_layout() command
"""
if(save): plt.savefig('ex3, fig2.png',dpi=mydpi)
plt.show()
cleaned=np.fft.ifft(z_filtered)
"""
ifft is the inverse FFT algorithm
it converts an fft graph back into a sinusoidal graph
we took the data, took the fft, used a filter function 
to eliminate most of the noise, then took the inverse fft
to get our "cleaned" version of the original data
"""
fig, (ax1,ax2,ax3)=plt.subplots(3,1,sharex='col',sharey='col')
ax1.plot(time/N,x)
ax2.plot(time/N,np.real(cleaned))
ax3.plot(time/N,y)
"""
we plot the real part of our cleaned data - but since the 
original data was real, the result of our tinkering should 
be real so we don't lose anything by doing this
if you don't explicitly plot the real part, python will 
do it anyway and give you a warning message about only
plotting the real part of a complex number. so really, 
it's just getting rid of a pesky warning message
"""
fig.subplots_adjust(hspace=0)
ax1.set_ylim(-13,13)
ax1.set_ylabel('Original Data')
ax2.set_ylabel('Filtered Data')
ax3.set_ylabel('Ideal Result')
ax3.set_xlabel('Position-Time')
plt.tight_layout() 

if(save): plt.savefig('ex3, fig3.png',dpi=mydpi)
plt.show()
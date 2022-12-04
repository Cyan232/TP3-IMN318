import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.io.wavfile as swav
from Hamming import *

#Paramêtre
M = 512
H = 128


samplerate, glock = swav.read("Glock.wav")
print("Sample rate : " + str(samplerate) + " hz")

result = np.zeros((M,len(glock)))
ham = Hamming(M,0.5)
for i in range(0,len(glock),H):
    if(i+M)< len(glock): 
        fft = np.fft.fft(np.multiply(ham,glock[i:i+M])) 
        result[:,i] = np.log(np.abs(np.real(fft)))

plt.plot(result)
plt.show()
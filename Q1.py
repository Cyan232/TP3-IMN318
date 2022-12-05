import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.io.wavfile as swav
from Hamming import *


#Paramêtre
M = 4096
H = 128

samplerate, glock = swav.read("Glock.wav")
print("Sample rate : " + str(samplerate) + " hz")

#result = np.zeros((M,np.int32(len(glock)/H)))
#fondamentals = np.zeros(np.int32(len(glock)/H))
ham = Hamming(M,0.5)

result = np.zeros((np.int32(M/2),np.int32(len(glock)/H)))

for i in range(len(glock)):
    if((i*H)+M)< len(glock): 
        fft = np.fft.fft(np.multiply(ham,glock[i*H:(i*H)+M]))
        fft =(np.log(np.real(np.abs(fft))))

        result[:,i] = fft[0:np.int32(M/2)]
        #result[:,i] = np.where((fft / np.max(fft)) > .5,fft,0)[0:np.int32(M/2)]
        #result[:,i] = result[:,i] * np.sum(fft)

        #---------TEST Alanyse cepstral--------------------
        #values = (np.fft.ifft(fft))
        #values = np.transpose(values)[0:M]

        #result[:,i] = values
        
plt.imshow(result, cmap='plasma')
plt.show()
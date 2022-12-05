import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.io.wavfile as swav
from Hamming import *

#Paramêtre
M = 512*8
H = 256

#fft = np.fft.fft(np.multiply(ham,glock[i*H:(i*H)+M]))[0:np.int32(M/2)]       
#result[:,i] = np.transpose(np.log(np.abs(np.real(fft))))

samplerate, glock = swav.read("Glock.wav")
print("Sample rate : " + str(samplerate) + " hz")

result = np.zeros((np.int32(M/2),np.int32(len(glock)/H)))
fondamentals = np.zeros(np.int32(len(glock)/H))
ham = Hamming(M,0.5)

for i in range(len(glock)):
    if((i*H)+M)< len(glock): 
        fft = np.fft.fft(np.multiply(ham,glock[i*H:(i*H)+M]))
        fft =(np.log(np.abs(np.real(fft))))
        result[:,i] = np.transpose(fft)[0:np.int32(M/2)]

#fft = np.log(np.abs(np.real(np.fft.fft(glock[0:M])))) 
#fft = np.log(((np.fft.fft(glock[0:M])**2)))
#ifft = np.fft.ifft(fft)

plt.imshow(result)
plt.show()

#plt.plot(ifft)
#plt.show()
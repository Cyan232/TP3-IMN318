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

ham = Hamming(M,0.5)

spectrum = np.zeros((np.int32(M/2),np.int32(len(glock)/H)))
notes = np.zeros((np.int32(M/2),np.int32(len(glock)/H)))

for i in range(len(glock)):
    if((i*H)+M)< len(glock): 
        fft = np.fft.fft(np.multiply(ham,glock[i*H:(i*H)+M]))
        fft =(np.log(np.real(np.abs(fft))))
        fft /= np.max(fft)
        temp = np.where(fft > .8 , 1, 0)
        notes[:,i] = temp[0:np.int32(M/2)]
        spectrum[:,i] = fft[0:np.int32(M/2)]

        
plt.imshow(spectrum, cmap='plasma')
plt.xlabel('Temps')
plt.ylabel('Fréquences')
plt.title('Spectogramme')
plt.show()
   
plt.imshow((spectrum * .25)+ notes , cmap='plasma')
plt.xlabel('Temps')
plt.ylabel('Fréquences')
plt.title('Spectogramme')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.io.wavfile as swav
from Hamming import *
import scipy.signal as signal

#Paramêtre
M = 4096
H = 128

samplerate, restore = swav.read("Restore.wav")
print("Sample rate : " + str(samplerate) + " hz")

ham = Hamming(M,0.5)
spectrum = np.zeros((np.int32(M/2),np.int32(len(restore)/H)))

#----Spectogramme son originale---------
for i in range(len(restore)):
    if((i*H)+M)< len(restore): 
        fft = np.fft.fft(np.multiply(ham,restore[i*H:(i*H)+M]))
        fft =(np.log(np.real(np.abs(fft))))
        spectrum[:,i] = fft[0:np.int32(M/2)]

plt.imshow(spectrum , cmap='plasma')
plt.xlabel('Temps')
plt.ylabel('Fréquences')
plt.title('Spectogramme')
plt.show()


#----Filtrage----------------------
bfilter,afilter = signal.butter(3,[460.0,530.0],btype='bandstop', fs=samplerate)
restore[44800:96000] = signal.lfilter(bfilter,afilter,restore[44800:96000])
swav.write("Restore filtré.wav", samplerate, np.int16(restore))

#----Spectogramme son fitré---------
for i in range(len(restore)):
    if((i*H)+M)< len(restore): 
        fft = np.fft.fft(np.multiply(ham,restore[i*H:(i*H)+M]))
        fft =(np.log(np.real(np.abs(fft))))
        spectrum[:,i] = fft[0:np.int32(M/2)]

plt.imshow(spectrum , cmap='plasma')
plt.xlabel('Temps')
plt.ylabel('Fréquences')
plt.title('Spectogramme')
plt.show()
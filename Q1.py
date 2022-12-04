import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.io.wavfile as swav

samplerate, glock = swav.read("Glock.wav")

print("Sample rate : " + str(samplerate) + " hz")

#plt.plot(glock)
#plt.show()
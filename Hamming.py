import numpy as np
#function pour la fenêtre Hamming
def Hamming(N,a):
    n = np.arange(-N/2,N/2,1)
    return a + (1.0-a)*np.cos((2*np.pi*n)/N)
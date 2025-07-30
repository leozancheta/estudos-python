import numpy as np

class ImplementsNumpy: 
    def criar_array(self, lista):
        return np.array(lista)
    
    def media(self, array):
        return np.mean(array)
    
    def desvio_padrao(self, array):
        return np.std(array)
    
    def soma(self, array):
        return np.sum(array)
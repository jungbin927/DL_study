import os 
import sys
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error

class simpletNet:
    def __init__(self):
        self.W=np.random.randn(2,3)
        
    def predict(self,x):
        return np.dot(x,self.w)
    
    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        
        return loss
import numpy as np 


class Evaluation:
    def __init__(self, ground_truth, predictions):
        self.yt = ground_truth
        self.yp = predictions
        self.yd = self.yt - self.yp
    
    def mae(self):
        return np.mean(self.yd)
        
    def mse(self):
        return np.mean(self.yd**2)
    
    def rmse(self):
        return np.sqrt(self.mse())
    
    def msle(self):
    
    def rae(self):
    
    def rse(self):
    
    def r2(self):
    

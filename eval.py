import numpy as np 


class Evaluation:
    def __init__(self, ground_truth, predictions):
        self.yt = ground_truth
        self.yp = predictions
        try:
            self.yd = self.yt - self.yp
            self.n  = len(self.yd)
        except ValueError:
            print("Vectors lenghts do not match.")
            raise
            
    def mae(self):
        return np.mean(np.abs(self.yd))
        
    def mse(self):
        return np.mean(self.yd**2)
    
    def rmse(self):
        return np.sqrt(self.mse())
    
    def msle(self):
        return np.mean(np.log((1 + self.yt) / (1 + self.yp))**2)
    
    def rae(self):
        return np.sum(np.abs(self.yt - self.yd)) / np.sum(np.abs(self.yt - np.mean(self.yt)))
        
    def rse(self):
        return np.sum(self.yt - self.yd)**2 / np.sum(self.yt - np.mean(self.yt))**2
    
    def r2(self):
        return 1 - self.rse()
    
    def mpe(self):
        return 100 * np.mean(self.yd / self.yt)
    
    def mape(self):
        return 100 * np.mean(np.abs(self.yd / self.yt))

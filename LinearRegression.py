import numpy as np

class linearRegression:
    b = [0,0]
    def train(self,x,y):
        mean_x = np.mean(x)
        mean_y = np.mean(y)
        m = len(x)
        numerator = 0
        denominator = 0
        for i in range(m):
            numerator+=(x[i]-mean_x)*(y[i]-mean_y)
            denominator += (x[i]-mean_x)**2
        b1 = numerator/denominator
        b0 = mean_y - (b1*mean_x)
        self.b = [b0,b1]
    def predict(self,z):
        result = self.b[0] + (self.b[1]*z)
        return result         
    
x = [1,2,3]
y = [2,4,6]
model = linearRegression()

model.train(x,y)
model.predict(9)
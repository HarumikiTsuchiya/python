
import numpy as np


class test():
    def __init__(self,a):
        self.a=a
    def print(self):
        b=([[1,2],[3,4]])
        #print(b)
        return b
    def t(self):
        N=4096
        dt = 0.0001

        t=np.arange(0,N*dt,dt)

        c=self.print()
        print(c)
        
        return t



f=test(2)
a=f.print()

t=f.t()

print(a)
print(t)


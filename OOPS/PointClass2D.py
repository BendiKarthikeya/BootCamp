import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def Print_point(self):
        print("x:",self.x,"y:",self.y)
    def dist_origin(self):
        return math.sqrt(self.x**2+self.y**2)
    def distance(self,P):
        return math.sqrt((self.x-P.x)**2+(self.y-P.y)**2)
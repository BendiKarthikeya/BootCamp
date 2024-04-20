import math
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def distance(self,otherPoint):
        dx=self.x-otherPoint.x
        dy=self.y-otherPoint.y
        dz=self.z-otherPoint.z
        distance=math.sqrt(dx**2+dy**2+dz**2)
        return distance
    
    def is_equal(self,otherPoint):
        distance1=origin.distance(self)
        distance2=origin.distance(otherPoint)
        if(distance1==distance2):
            return True
        else:
            return False
        
    def dot(self,otherPoint):
        dot_Product= self.x*otherPoint.x + self.y*otherPoint.y + self.z*otherPoint.z
        return dot_Product

    def unitVector(self):
        ux=self.x/origin.distance(self)
        uy=self.y/origin.distance(self)
        uz=self.z/origin.distance(self)
        return ux,uy,uz

point1 = Point(1, 2, 3)
point2 = Point(4, 5, 6)
origin = Point(0,0,0)

# distance = point1.distance(point2)
# print("Distance between point1 and point2:", distance)

# distance_from_origin=origin.distance(point1)
# print("Distance between origin and point1:", distance_from_origin)

# distance_from_origin=origin.distance(point2)
# print("Distance between origin and point2:", distance_from_origin)

# is_equal = point1.is_equal(point2)
# print("is_equal point1 and point2:", is_equal)

# dotProduct= point1.dot(point2)
# print("dotProduct between point1 and point2:", dotProduct)
        
# unitVector=point1.unitVector()
# print(unitVector)


# import math

# class Vector3D:
#     def __init__(self, x, y, z):
#         self.X=x
#         self.Y=y
#         self.Z=z
#     def __str__(self):
#         return "X: {0}, Y: {1}, Z: {2}".format(self.X, self.Y, self.Z)
        
#     def get_len(self):
#         return math.sqrt(self.X**2+self.Y**2+self.Z**2)
    
#     @staticmethod
#     def dot(self, other):
#         return self.X*other.X+self.Y*other.Y+self.Z*other.Z
# v1=Vector3D(10, 10, 0)
# v2=Vector3D(20, 10, 0)
# print(Vector3D.dot(v1, v2))
# print(v1.get_len())
# print(v2.get_len())
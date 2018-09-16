# import PrivateFunction
# print(PrivateFunction.x)
# 有警告
# print(PrivateFunction._y)
# 可以访问
# print(PrivateFunction.__k)
from object.PrivateFunction import *
print(x)
# 有__all__访问会有警告
# 没有__all__访问不了
print(_y)

print(__k)
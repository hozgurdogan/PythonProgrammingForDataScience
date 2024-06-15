import numpy as np

np.array([1,2,3,4,5])
print(type(np.array([1,2,3,4,5])))


np.zeros(100,dtype=float)
print(np.zeros(100,dtype=float))


print(np.random.randint(0,10,size=10))


# belirili bir istatistiksel veriye göre rastegele değer üretmek

np.random.normal(10.12,4,(3,4))
print(np.random.normal(10.12,4,(3,4)))
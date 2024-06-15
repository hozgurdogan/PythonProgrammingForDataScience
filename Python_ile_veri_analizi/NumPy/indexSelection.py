import numpy as np

a = np.random.randint(0,10 , size = 10 )

print(a[0:5])
print("000000000000000000000000000000000000000000000")

m =  np.random.randint(0,10, size=(3,5) )
print(m)

print(m[1,1])

#1.satırın tüm satünlarını seç

print(m[0:1,:])
import numpy as np

# ndim : boyut sayısı
# shape : boyut bilgisi
# size : toplam eleman sayısı
# dtype : array veri tipi

a = np.random.randint(0,10 , size=5)
print(a)

print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
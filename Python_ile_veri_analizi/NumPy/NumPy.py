#Numpy arraylerinin list yapılarınından farklılaştığı 2 temel yer :
# 1- Verimli veri saklama ( tek tip veri saklar , sabit tipte veri tutar  )

# 2- Vektörel işlemler yüksek seviyeden işlem yapabilme kapasitesi


import numpy as np


a = [1,2,3,4]
b = [2,3,4,5]

ab = []
# iki listeyi çarpmnak için iki listeyi gezip çarpıp boş listeye atmamız gerek

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

print(ab)


# bu klasik yoldan ziyade numPy ile yapalım birde

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a*b)



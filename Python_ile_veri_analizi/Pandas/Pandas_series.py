################################
#   Pandas Series (tek boyutlu)
################################

import pandas as pd

# Bir Pandas Series (tek boyutlu) oluşturma
s = pd.Series([1, 2, 3, 4, 5])

# Series'in tipini yazdırma
print(type(s))

# Series'in indekslerini yazdırma
print(s.index)

# Series'in veri tipini yazdırma
print(s.dtype)

# Series'in eleman sayısını yazdırma
print(s.size)

# Series'in boyut sayısını yazdırma (tek boyutlu olduğu için 1 döner)
print(s.ndim)

# Series'in değerlerini numpy array olarak yazdırma
print(s.values)

# Series'in değerlerinin tipini yazdırma
print(type(s.values))

# Series'in ilk 2 elemanını yazdırma
print(s.head(2))

# Series'in son 2 elemanını yazdırma
print(s.tail(2))

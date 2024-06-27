############################
# Birleştirme işlemleri
############################

import numpy as np
import pandas as pd

# 1 ile 30 arasında rastgele tam sayılar içeren 5x3 boyutunda bir NumPy array oluşturma
m = np.random.randint(1, 30, size=(5, 3))

# NumPy array'ini bir DataFrame'e dönüştürme ve sütun adlarını belirleme
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])

# df1'in değerlerine 99 ekleyerek yeni bir DataFrame oluşturma
df2 = df1 + 99

# İki DataFrame'i alt alta birleştirme , indeksleri sıfırlama
result = pd.concat([df1, df2], ignore_index=True)

# Birleştirilmiş DataFrame'i yazdırma
print(result)

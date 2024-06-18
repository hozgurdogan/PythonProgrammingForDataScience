###########################################
#  Quick_Look_At_Data (Veriye hızlı bakış)
###########################################

import pandas as pd
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk 5 satırını yazdırma
df.head()

# DataFrame'in son 5 satırını yazdırma
df.tail()

# DataFrame'in boyutlarını yazdırma (satır ve sütun sayısı)
df.shape

# DataFrame hakkında genel bilgi yazdırma (sütun isimleri, veri tipleri, null değerler vb.)
df.info()

# DataFrame'in sütun isimlerini yazdırma
df.columns

# DataFrame'in özet istatistiklerini yazdırma ve transpoze etme (daha okunabilir hale getirme)
df.describe().T

""" 
count-----> kaç gözlemden oluştuğu bilgisi 
mean -----> ortalaması 
std  -----> standart sapması 
min  -----> minimum değeri 
25%  -----> birinci çeyreklik değeri 
50%  -----> medyan (ikinci çeyreklik) değeri 
75%  -----> üçüncü çeyreklik değeri 
max  -----> maksimum değeri 
"""

# DataFrame'deki her bir sütunda bulunan eksik değerlerin sayısını yazdırma
df.isnull().sum()

# 'sex' sütununun ilk 5 değerini yazdırma
df["sex"].head()

# 'sex' sütunundaki değerlerin frekans dağılımını yazdırma
df["sex"].value_counts()

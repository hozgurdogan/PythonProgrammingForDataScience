import pandas as pd
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk 5 satırını yazdırma
print("İlk 5 satır:\n", df.head())

# DataFrame'in indekslerini yazdırma
print("DataFrame'in indeksleri:\n", df.index)

# DataFrame'in 0'dan 13'e kadar olan satırlarını yazdırma (13 dahil değil)
print("İlk 13 satır:\n", df[0:13])

# İndeksi 1 olan satırı silip kalan ilk 5 satırı yazdırma (geçici)
print("İndeksi 1 olan satırı silip kalan ilk 5 satır (geçici):\n", df.drop(1, axis=0).head())

# Silmek için indekslerin listesi
delete_index = [1, 3]

# İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satırı yazdırma (geçici)
print("İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satır (geçici):\n", df.drop(delete_index, axis=0).head())  # kalıcı değil

# İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satırı yazdırma (kalıcı)
df.drop(delete_index, axis=0, inplace=True)
print("İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satır (kalıcı):\n", df.head())  # kalıcı, aynı df=df.drop(delete_index, axis=0).head() işlemi gibi

##############################
#   Değişkeni indexe çevirme
##############################

# 'age' sütununun ilk 5 satırını yazdırma
print("Yaş sütununun ilk 5 satırı:\n", df["age"].head())

# 'age' sütununu indeks olarak ayarlama
df.index = df["age"]

# 'age' sütununu DataFrame'den kaldırma
df.drop("age", axis=1, inplace=True)

########################

# 'age' sütununu tekrar DataFrame'e ekleyerek indeks olarak ayarlama
df["age"] = df.index

# DataFrame'i yazdırma
print(df)

# 'age' sütununu tekrar kaldırma
df.drop("age", axis=1, inplace=True)

###################################
# 2. yol
################################

# İndeksleri sıfırlama ve DataFrame'in ilk 5 satırını yazdırma
df = df.reset_index().head()
print(df)

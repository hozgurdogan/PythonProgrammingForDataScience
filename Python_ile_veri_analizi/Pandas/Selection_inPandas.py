import pandas as pd
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk 5 satırını yazdırma
df.head()

# DataFrame'in indekslerini yazdırma
df.index

# DataFrame'in 0'dan 13'e kadar olan satırlarını yazdırma (13 dahil değil)
df[0:13]

# İndeksi 1 olan satırı silip kalan ilk 5 satırı yazdırma (geçici)
df.drop(1, axis=0).head()

# Silmek için indekslerin listesi
delete_index = [1, 3]

# İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satırı yazdırma (geçici)
df.drop(delete_index, axis=0).head()  # kalıcı değil

# İndeksi 1 ve 3 olan satırları silip kalan ilk 5 satırı yazdırma (kalıcı)
df.drop(delete_index, axis=0, inplace=True).head()  # kalıcı, aynı df=df.drop(delete_index, axis=0).head() işlemi gibi

import pandas as pd
import seaborn as sns

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# DataFrame'in ilk 5 satırını yazdırma
print("İlk 5 satır:\n", df.head())

# "age" sütununun iki katı olan yeni bir sütun ekleme
df["age2"] = df["age"] * 2

# "age" sütununun beş katı olan yeni bir sütun ekleme
df["age3"] = df["age"] * 5

# Yeni sütunlarla birlikte DataFrame'in ilk 5 satırını yazdırma
print("Yeni sütunlarla birlikte ilk 5 satır:\n", df.head())

# DataFrame'deki her bir sütun için
for col in df.columns:
    # Eğer sütun ismi "age" içeriyorsa
    if "age" in col:
        # Sütunun tüm değerlerini 10'a bölme
        df[col] = df[col] / 10

# Değişikliklerden sonra DataFrame'in tamamını yazdırma
print("Yaş sütunları 10'a bölündükten sonra:\n", df)

#######
# "age" içeren sütunları seçip her birini 10'a bölen lambda fonksiyonu uygulama ve ilk 5 satırı yazdırma
print("Lambda fonksiyonu ile 10'a bölünmüş yaş sütunlarının ilk 5 satırı:\n", df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head())

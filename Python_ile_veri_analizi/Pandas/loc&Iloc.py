############################
# iloc ve loc kullanımı
############################

import pandas as pd
import seaborn as sns

# Tüm sütunların gösterilmesi için pandas ayarını yapma
pd.set_option('display.max_columns', None)

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")

# iloc: integer based selection (integer tabanlı seçim)

# İlk 3 satırı seçme (0'dan 3'e kadar, 3 dahil değil)
print("df.iloc[0:3] ile ilk 3 satır:\n", df.iloc[0:3])

# İlk 2 satırı ve ilk 3 sütunu seçme (0'dan 2'ye kadar satırlar ve 0'dan 3'e kadar sütunlar, her ikisi de dahil değil)
print("df.iloc[0:2, 0:3] ile ilk 2 satır ve ilk 3 sütun:\n", df.iloc[0:2, 0:3])

# loc : label based selection (etiket tabanlı seçim)

# İlk 4 satırı seçme (0'dan 3'e kadar, 3 dahil)
print("df.loc[0:3] ile ilk 4 satır:\n", df.loc[0:3])

# Satırlardan 0'dan 3'e kadar gitmek ve belirli bir sütun seçmek

# iloc: (hata verir çünkü iloc integer bazlı seçimde hem satır hem sütun indeksleri gerektirir)
try:
    df.iloc[0:4, "age"]
except Exception as e:
    print("df.iloc[0:4, 'age'] hatası:\n", e)

# loc: (etiket bazlı seçimde doğru kullanım)
print("df.loc[0:3, 'age'] ile ilk 4 satırın 'age' sütunu:\n", df.loc[0:3, "age"])

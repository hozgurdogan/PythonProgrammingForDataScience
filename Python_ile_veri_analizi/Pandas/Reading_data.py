#################################
#   Reading data (veri okuma)
#################################

import pandas as pd

# 'advertising.csv' dosyasını okuyarak bir DataFrame oluşturma
df = pd.read_csv("./advertising.csv")

# DataFrame'in ilk 5 satırını yazdırma
print(df.head())

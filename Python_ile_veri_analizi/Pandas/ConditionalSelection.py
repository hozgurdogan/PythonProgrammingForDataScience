
import pandas as pd
import seaborn as sns

# Tüm sütunların gösterilmesi için pandas ayarını yapma
pd.set_option('display.max_columns', None)

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")


df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50 , ["age","class","sex"]].head() # 1 koşşulu hali


df.loc[(df["age"] > 50)
       & (df["sex"] == 'male') ,
       ["age","class","sex"]].head()
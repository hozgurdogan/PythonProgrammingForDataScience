'''
-count
-first
-last
-mean
-median
-min
-max
-std
-var
-sum
-pivot table
'''



import pandas as pd
import seaborn as sns

# Tüm sütunların gösterilmesi için pandas ayarını yapma
pd.set_option('display.max_columns', None)

# Titanic veri setini yükleme
df = sns.load_dataset("titanic")
df.head()

#yaş ortlaması
df["age"].mean()

#cinseyete göre yaş ortlaması

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age":["mean","sum"]}) ####önemli bu daha mantıklı


df.groupby(["sex","embark_town","class"]).agg({
    "age":["mean"],
    "survived":"mean",
    "sex":"count"}) ####önemli bu daha mantıklı


#sayısal değişkeni katagorik değişkene dönüştrüme
df["new_age"]=pd.cut(df["age"],[0,10,18,25,30,90])
df.head()

#############################################################
#               Pivot Table
#############################################################

df.pivot_table("survived","sex",["new_age","class"])


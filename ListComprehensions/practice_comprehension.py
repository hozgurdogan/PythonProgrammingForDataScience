##########################################
#   UYGULAMA MÜLAKAT SORUSU
##########################################

# Amaç çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir

# 0'dan 9'a kadar olan sayıları içeren bir range nesnesi oluşturma
numbers = range(10)

# numbers değişkeninin tipini kontrol etme
type(numbers)

# Yeni bir sözlük oluşturma
newDict = {}

# Her bir sayı için işlem yapma
for number in numbers:
    # Sayı çiftse, sayının karesini sözlüğe ekle
    if number % 2 == 0:
        newDict[number] = number ** 2
    # Sayı tekse, sayıyı sözlüğe ekle
    else:
        newDict[number] = number

##################################################33333
# List comprehension kullanarak daha kısa bir yöntem
{number: number ** 2 if number % 2 == 0 else number for number in numbers}

###################################################################
#   pratice 2
# Kolon isimlerimni tüm harflerini büyük harfli yapmak!
###################################################################

import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.columns)

# KLASİK YOL

# Boş bir liste oluşturma
A = []

# Her bir kolon ismi için büyük harf yapma ve listeye ekleme
for col in df.columns:
    A.append(col.upper())

# Yeni kolon isimlerini DataFrame'e atama
df.columns = A

# Yeni kolon isimlerini kontrol etme
df.columns

# List comprehension kullanarak daha kısa bir yöntem
df.columns = [col.upper() for col in df.columns]

print("İstediğim yöntem ile..........." + df.columns)

#####################################################
# Pratice 3 ----- İsiminde "ins" olan değişkenlerin başına FLAG diğerlerinin başına NO_FLAG eklemek istiyoruz.
#####################################################

# Her bir kolon adını kontrol ederek "INS" içerip içermediğini kontrol edin ve buna göre "FLAG_" veya "NO_FLAG_" ekleyin
df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

# Yeni kolon adlarını kontrol etme
print(df.columns)

##############
# Practice 3
# Amaç key'i string ,value'su aşağıdaki gibi bir liste olan sözlük oluşturmak
# Sadece sayısal değişkenler için yapmak istiyoruz

################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_losses': ['mean', 'min', 'max', 'var']}

import seaborn as sns

# Veri setini yükleme
df = sns.load_dataset("car_crashes")

# Kolon isimlerini kontrol etme
df.columns

# Sayısal verileri sütunlardan çekme
num_cols = [col for col in df.columns if df[col].dtype.kind in 'if']
print(num_cols)

# Yeni bir sözlük oluşturma
soz = {}
agg_list = ["mean", "min", "max", "sum"]

# Her bir sayısal kolon için işlem yapma
for col in num_cols:
    soz[col] = agg_list
print(soz)

# List comprehension kullanarak daha kısa bir yöntem
new_dict = {col: agg_list for col in num_cols}

# Sayısal kolonların ilk birkaç satırını gösterme
print(df[num_cols].head())

# Agg fonksiyonu ile işlemleri gerçekleştirme
df[num_cols].agg(new_dict)

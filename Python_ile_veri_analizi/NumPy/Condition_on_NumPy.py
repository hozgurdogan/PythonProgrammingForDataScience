#######################################
# Condition on NumPy
#######################################

import numpy as np

# 1'den 5'e kadar olan sayıları içeren bir NumPy array oluşturma
v = np.array([1, 2, 3, 4, 5])

# List comprehension kullanarak 3'ten küçük sayıları filtreleme
ab = [num for num in v if num < 3]

# Filtrelenmiş sayıları yazdırma
print(ab)

# NumPy ile doğrudan koşullu filtreleme
# 3'ten küçük sayılar için boolean mask oluşturma
print(v < 3)

# Boolean mask kullanarak 3'ten küçük sayıları filtreleme ve yazdırma
print(v[v < 3])


import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr)
print('1. boyuttaki 2.eleman: ', arr[0, 1])


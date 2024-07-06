import keras
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image

# Kaydedilmiş modeli yükle
model = load_model('cnn_model.h5')

# Tahmin edilecek resmin dosya yolu
img_path = '3.png'

# Resmi yükle, yeniden boyutlandır ve normalleştir
img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')
img_array = image.img_to_array(img)
img_array = img_array.reshape(1, 28, 28, 1).astype('float32') / 255

# Model ile tahmin yap
predicted_class = model.predict(img_array)
predicted_class = np.argmax(predicted_class, axis=1)

# Tahmin edilen sınıfı yazdır
print(f"Predicted Class: {predicted_class[0]}")

# Tahmin edilen resmi göster
plt.imshow(img_array.reshape(28, 28), cmap='gray')
plt.title(f"Predicted Label: {predicted_class[0]}")
plt.axis('off')
plt.show()

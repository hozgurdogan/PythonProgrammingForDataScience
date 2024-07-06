from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image

# Load the pretrained model
pretrained_model = load_model('classification_model.h5')

# Load and preprocess the example image ('deneme.png' in this case)
img_path = '3.png'
img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')  # Load image and resize to model's input shape
img_array = image.img_to_array(img)  # Convert image to numpy array
img_array = img_array.astype('float32') / 255.0  # Normalize pixel values to [0, 1]
img_array = img_array.reshape(1, 28*28)  # Flatten and reshape to match input shape (assuming 28x28 images)

# Perform prediction
predictions = pretrained_model.predict(img_array)
predicted_class = np.argmax(predictions)

# Print the predicted class
print(f'Predicted class: {predicted_class}')


'''predictions = pretrained_model.predict(img_array):

pretrained_model.predict(img_array) komutu, pretrained_model adlı önceden eğitilmiş modele img_array adlı görüntüyü verir.
Model, bu görüntü üzerinde sınıflandırma yaparak sınıf olasılıklarını içeren bir tahmin vektörü (predictions) döndürür.
predicted_class = np.argmax(predictions):

np.argmax(predictions) komutu, predictions adlı tahmin vektöründeki en yüksek olasılığa sahip sınıfın indeksini bulur.
Bu indeks, görüntünün tahmin edilen sınıfını temsil eder. Yani, tahmin edilen sınıfın sayısal olarak belirtilmiş bir indeksi (predicted_class) olur.'''
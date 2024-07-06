import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import matplotlib.pyplot as plt

# import the data
from keras.datasets import mnist

#read the data
(X_train , y_train ), (X_test , y_test ) = mnist.load_data()

print(X_train.shape)
print(X_test.shape)

plt.imshow(X_train[2])
print(y_train[2])
plt.show()  # Grafiğin ekranda kalmasını sağlar

#   With conventional neural networks, we cannot feed in the image as input as is. So we need to
#   flatten the images into one-dimensional vectors, each of size 1 x (28 x 28) = 1 x 784.

num_pixcels = X_train.shape[1] * X_train.shape[2] # find size of one-dimensional vector

X_train = X_train.reshape(X_train.shape[0] , num_pixcels).astype('float32') #flatten training images # X_train.shape = (60000, 784)

X_test = X_test.reshape(X_test.shape[0] , num_pixcels).astype('float32')

print(X_test[1])

# Since pixel values can range from 0 to 255, let's normalize the vectors to be between 0 and 1.

X_train = X_train / 255
X_test =  X_test /255

#Finally, before we start building our model, remember that for classification we need to divide our target variable into categories. We use the to_categorical function from the Keras Utilities package.


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)


num_classes = y_test.shape[1]
print(num_classes)

#Build a Neural Network¶


def classification_models():
    model = Sequential()
    model.add(Dense(num_pixcels , activation = 'relu', input_shape = (num_pixcels , )))
    model.add(Dense(100,activation = 'relu'))
    model.add(Dense(250,activation = 'relu'))

    model.add(Dense(num_classes , activation = 'softmax')) # sınıflndırma katmanı

    #compile model
    model.compile(optimizer = 'adam' , loss = 'categorical_crossentropy' , metrics = ['accuracy'])

    return model


# Train and Test the Network



model = classification_models()

model.fit(X_train , y_train , validation_data = (X_test , y_test) , epochs = 50 , verbose = 2)


score = model.evaluate(X_test , y_test , verbose = 0)


print('Accuracy : {} \n Error : {}'.format(score[1],1-score[1]))

model.save('classification_model.h5')
import pandas as pd
import numpy as np

#Let's download the data and read it into a pandas dataframe.


concrete_data = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv')
print(concrete_data.head())

print(concrete_data.shape)

#So, there are approximately 1000 samples to train our model on.
#Because of the few samples, we have to be careful not to overfit the training data.


print(concrete_data.describe().T)


#Let's check the dataset for any missing values.


print(concrete_data.isnull().sum())




# Split data into predictors and target

#The target variable in this problem is the concrete sample strength.
# Therefore, our predictors will be all the other columns.


concrete_data_columns = concrete_data.columns

print(concrete_data_columns)

predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']]

# predictors1 = concrete_data.iloc[:,:-1]

print(predictors)
# target

target = concrete_data['Strength']
print(target)


#Finally, the last step is to normalize the data by substracting the mean and dividing by the standard deviation.


predictors_norm = (predictors - predictors.mean()) /predictors.std()

print(predictors_norm.head())

#Let's save the number of predictors to n_cols since we will need this number when building our network.

n_cols = predictors_norm.shape[1]
print(n_cols)

#Let's go ahead and import the Keras library

from keras.models import Sequential
from keras.layers import Dense


# define regression model
def regression_model():
    # create model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))

    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


# build the model
model = regression_model()

# fit the mode
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)
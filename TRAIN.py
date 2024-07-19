''' USE THIS TO TRAIN YOUR MODEL'''

# IMPORTS
from __future__ import print_function
import keras
from keras.datasets import mnist # type: ignore
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Dropout, Flatten # type: ignore
from keras.layers import Conv2D, MaxPooling2D # type: ignore
from keras import backend as K # type: ignore

# HYPERPARAMETERS idk why theyre called hyperparameters
batch_size = 128
num_classes = 10 #10 classes 0,1,2,3,4,5,6,7,8,9
epochs = 10

# you pass a 28x28 image to yo model, u baka
img_rows, img_cols = 28, 28

# KERAS DOCUMENTATION
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# KERAS DOCUMENTATION
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Image Normalization from KERAS DOCUMENTATION
x_train /= 255
x_test /= 255

# One Hot Encoding from KERAS DOCUMENTATION
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# keras.seqential model 

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))

# CONV (hidden layers)
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))

# POOL
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())

# Fully connected lauyers
model.add(Dense(128, activation='relu'))
# model.add(Dense(64, activation='relu'))

# MAKE SURE THE OUTPUT LAYER IS ALWAYS EQUAL TO THE NUM OF CLASSES
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy, optimizer=keras.optimizers.SGD(learning_rate=0.01), metrics=['accuracy'])
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('\nTest loss:', score[0])
print('\nTest accuracy:', score[1])

model.save('digits.h5')


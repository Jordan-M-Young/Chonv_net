from tensorflow.python.client import device_lib 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator


"""Example 3 of how a model can be trained, this script explicitly calls
various tensorflow model layers to design a custom model architecture. This
style of model construction sacrifices the ability to train multiple models
of differing architectures for more control over a single model's architecture."""


#Model Result Metrics
accs = []
val_accs = []
losses = []
val_losses = []


#Builds Image generators used to pass images to model for training/validation
train_datagen = ImageDataGenerator(
        rescale=1./255,
        horizontal_flip=True,
        vertical_flip=True
        )

test_datagen = ImageDataGenerator(
        rescale=1./255,
        horizontal_flip=True,
        vertical_flip=True
        )

train_generator = train_datagen.flow_from_directory(
        'C:/Users/jmyou/Desktop/Gen_Images_512_BIGSET_wnames/Train',
        target_size=(512, 512),
        color_mode="grayscale",
        shuffle=True,
        seed=20,
        batch_size=32,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        'C:/Users/jmyou/Desktop/Gen_Images_512_BIGSET_wnames/Validation',
        target_size=(512, 512),
        color_mode="grayscale",
        batch_size=32,
        shuffle=True,
        seed=33,
        class_mode='categorical')


# Generates Model Architecture
model = Sequential()

model.add(Conv2D(32, (2,2), input_shape = (512,512,1)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32, (2,2)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Flatten())


model.add(Dense(4))
model.add(Activation('softmax'))


#Compiles Model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#Trains model
model.fit_generator(
        train_generator,
        steps_per_epoch=100,
        epochs=5,
        validation_data=validation_generator,
        validation_steps=40)


#Records Training metrics
accs.append(model.history.history['accuracy'])
val_accs.append(model.history.history['val_accuracy'])
losses.append(model.history.history['loss'])
val_losses.append(model.history.history['val_loss'])

# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:08:28 2020

@author: jmyou
"""
from tensorflow.python.client import device_lib 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

#Custom Scripts
import chonv_zoo as cv
"""This script is an example of how I trained CNNs for the purpose of classifying my Ordinary Chondrite Image set. 
This script uses data generators and the flow from dir tensorflow method. To learn how to set up a compatible directory
for this method, see the readme. Model architectures were called from the chonv_zoo.py file"""

#Model Result Metrics
accs = []
val_accs = []
losses = []
val_losses = []

#Locations of your Training and Validation image sets 
train_dir_path = 'C:/Users/jmyou/Desktop/Gen_Images_512_BIGSET_wnames/Train'
val_dir_path = 'C:/Users/jmyou/Desktop/Gen_Images_512_BIGSET_wnames/Validation'


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
        train_dir_path,
        target_size=(512, 512),
        color_mode="grayscale",
        shuffle=True,
        seed=20,
        batch_size=32,
        class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
        val_dir_path,
        target_size=(512, 512),
        color_mode="grayscale",
        batch_size=32,
        shuffle=True,
        seed=33,
        class_mode='categorical')


# Generates Model Architecture any model from chonv_zoo.py is acceptable as a call here, C3D3 is only an example.
model = cv.C3D3(512)


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

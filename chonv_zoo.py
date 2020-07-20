# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 07:38:44 2020

@author: jmyou
"""


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D



def C1D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C1D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
  
    return model
    
def C1D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
   
    
    return model

def C1D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    
    return model

def C1D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    return model

def C1D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    return model

def C1D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    return model

def C1D8(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (2,2), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
    
    return model

def C2D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C2D8(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C3D8(img_size):
    
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C4D8(img_size):
    
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C5D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C5D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model


def C5D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C5D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C5D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model


def C5D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model


def C5D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C5D8(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C6D8(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D1(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D2(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D3(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D4(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D5(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D6(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D7(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model

def C7D8(img_size):
    
    model = Sequential()
    model.add(Conv2D(32, (3,3), input_shape = (img_size,img_size,1)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(32, (2,2)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(32))
    model.add(Activation('relu'))
    
    model.add(Dense(4))
    model.add(Activation('softmax'))
   
    
    return model
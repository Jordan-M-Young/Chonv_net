# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:22:53 2020

@author: jmyou
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D



def set_conv_defaults():
    
    """Sets convolutional layer parameters to these default values"""
    
    filters = 32
    filter_kernel_size = (3,3)
    activation = 'relu'
    pool_kernel_size = (2,2)
    
    return filters,filter_kernel_size,activation,pool_kernel_size

def conv_param_check(conv_params,i):
    
    """Checks to see if (1) a convolutional layer parameter dictionary has been
    passed to the model architecture constructor and (2) the layer being added
    had a corresponding paremeter set in the passed dictionary"""
    
    if conv_params == None:
        filters,filter_kernel_size,activation,pool_kernel_size = set_conv_defaults()
        
    else:
         try:
            filters = conv_params[str(i)]['filters']
            filter_kernel_size = conv_params[str(i)]['filter_kernel_size']
            activation = conv_params[str(i)]['activation']
            pool_kernel_size = conv_params[str(i)]['pool_kernel_size']
         except KeyError:
            filters,filter_kernel_size,activation,pool_kernel_size = set_conv_defaults()
            
    
    return filters,filter_kernel_size,activation,pool_kernel_size
 
def set_dense_defaults():
    
    """Sets dense layer parameters to these default values"""
    
    nodes = 32
    activation = 'relu'
    
    
    return nodes, activation

def dense_param_check(dense_params,i):
    
    """Checks to see if (1) a dense layer parameter dictionary has been
    passed to the model architecture constructor and (2) the layer being added
    had a corresponding paremeter set in the passed dictionary"""
    
    
    
    if dense_params == None:
        nodes, activation = set_dense_defaults()
    else:
        try:
            nodes = dense_params[str(i)]['nodes']
            activation = dense_params[str(i)]['activation']
        except KeyError:
            nodes, activation = set_dense_defaults()
    
    return nodes, activation


def model_architecture_constructor(imdim,conv_layers,dense_layers,classes=4,
                                   conv_params=None,dense_params=None):

    """constructs a convolutional neural network architecture based on the 
    following passed paramters:
        (1) Image dimension ---> imdim
        (2) #Convolutional Layers ---- > conv_layers
        (3) #Fully connected dense layers ---> dense_layers
        (4) #Image classes images are grouped into
        (5) Convolutional Layers parameter dictionary --> conv_params
        (6) Dense Layers parameter dictionary ---> dense_params"""

    
    model = Sequential()
    
    for i in range(conv_layers):
        if i == 0:
            parms = conv_param_check(conv_params,i)
            
            model.add(Conv2D(parms[0], parms[1],input_shape = (imdim,imdim,1)))
            model.add(Activation(parms[2]))
            model.add(MaxPooling2D(pool_size=parms[3]))
        else:
            parms = conv_param_check(conv_params,i)
            
            model.add(Conv2D(parms[0], parms[1]))
            model.add(Activation(parms[2]))
            model.add(MaxPooling2D(pool_size=parms[3]))
    
    model.add(Flatten())
    
    
    for i in range(dense_layers):
        if i == len(dense_layers) - 1:
            
            model.add(Dense(classes))
            model.add(Activation('softmax'))
        else:
            parms = dense_param_check(dense_params, i)
            model.add(Dense(parms[0]))
            model.add(Activation(parms[1]))
    

    return model
    
    
    
    
conv_params = {'0':{'filters':32,
                    'filter_kernel_size':(3,3),
                    'activation':'relu',
                    'pool_kernel_size':(2,2)},
               '1':{'filters':32,
                    'filter_kernel_size':(3,3),
                    'activation':'relu',
                    'pool_kernel_size':(2,2)}}


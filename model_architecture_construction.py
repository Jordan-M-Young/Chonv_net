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
    had a corresponding paremeter set in the passed dictionary.If either 
    (1) or (2) are untrue then that layer is set to the default values shown
    in set_conv_defaults"""
    
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
    had a corresponding paremeter set in the passed dictionary. If either 
    (1) or (2) are untrue then that layer is set to the default values shown
    in set_dense_defaults"""
    
    
    
    if dense_params == None:
        nodes, activation = set_dense_defaults()
    else:
        try:
            nodes = dense_params[str(i)]['nodes']
            activation = dense_params[str(i)]['activation']
        except KeyError:
            nodes, activation = set_dense_defaults()
    
    return nodes, activation


def add_conv_layers(model,conv_layers,conv_params,imdim):
    
    """Handles adding convolutional layers to model architecture"""
    
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
    
    return model


def add_dense_layers(model,dense_layers,dense_params,classes):
    
    """Handles adding dense layers to model architectures"""
    
    for i in range(dense_layers):
        if i == len(dense_layers) - 1:
            
            model.add(Dense(classes))
            model.add(Activation('softmax'))
        else:
            parms = dense_param_check(dense_params, i)
            model.add(Dense(parms[0]))
            model.add(Activation(parms[1]))
            
    return model

def model_architecture_constructor(imdim,conv_layers,dense_layers,classes=4,
                                   conv_params=None,dense_params=None):

    """constructs a convolutional neural network architecture based on the 
    following passed paramters:
        (1) Image dimension ---> imdim
        (2) #Convolutional Layers ---- > conv_layers
        (3) #Fully connected dense layers ---> dense_layers
        (4) #Image classes images are grouped into
        (5) Convolutional Layers parameter dictionary --> conv_params
        (6) Dense Layers parameter dictionary ---> dense_params
        
     Example conv_params dictionary:
    
    
     conv_params = {'0':{'filters':32,
                         'filter_kernel_size':(3,3),
                         'activation':'relu',
                         'pool_kernel_size':(2,2)},
                    '1':{'filters':32,
                         'filter_kernel_size':(3,3),
                         'activation':'relu',
                         'pool_kernel_size':(2,2)}
                    }
                    
                    
       If a conv_params dictionary has fewer entries than the number of conv layers
       specified, the unspecified layer will be given default parameters as seen in set_conv_default().
       The layer key strings must be entered as seen in the example;'filters' value  must be an integer;
       'filter_kernel_size' value must be a (n,m) tuple; 'activation' value must be a string; 'relu','softmax','sigmoid',
       etc; 'pool_kernel_size' must be a (n,m) tuple
        
        
        Example dense_params dictionary:
        
        dense_params = {'0':{'nodes':32,
                             'activation':'relu'},
                        '1':{'nodes':64,
                             'activation':'relu'}
                        }
        
        A dense param dictionary needs dense_layers - 1 entries at max. This is because the final dense layer 
        is the model output layer with nodes = image classes and a softmax activation layer. This activation 
        was chose due to the categorical nature of the model output layer. If #dense_param entries = dense_layers
        the last entry will be ignored. If a non output layer entry is is omitted then that layer will have default
        paremters as shown in set_dense_default(). The layer key strings must be entered as seen in the example;
        'nodes' value must be an integer;'activation' value must be a string.
        
        
        """
    
    #initializes the sequential model
    model = Sequential()
    
    #adds convolutional layers to the sequential model
    model = add_conv_layers(model,conv_layers,conv_params,imdim)
    
    #adds a flatten layer to model, this is the "bridge" between convoluted
    #feature maps and the fully connected neural network layers
    model.add(Flatten())
    
    #adds fully connected "dense" neural network layers
    model = add_dense_layers(model,dense_layers,dense_params,classes)
    

    return model

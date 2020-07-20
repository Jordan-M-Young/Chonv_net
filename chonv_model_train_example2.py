from tensorflow.python.client import device_lib 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

#Custom Scripts
import Model_Architecture_Construction as mac

"""Second example on how models can be trained, this example uses the 
model_architecture_constructor function, which gives the user more control
over architecture parameters. This function also allows one to iterate over lists
of parameters which allows for grid search style training regiments """

#Model Result Metrics
accs = []
val_accs = []
losses = []
val_losses = []

#Model Architecture parameters; see model_architecture_constructor for conv_params/dense_params guidelines
imdim = 512
conv_layers = 2
dense_layers = 2
classes = 4
conv_params = {'0':{'filters':32,
                    'filter_kernel_size':(3,3),
                    'activation':'relu',
                    'pool_kernel_size':(2,2)},
               '1':{'filters':32,
                    'filter_kernel_size':(3,3),
                    'activation':'relu',
                    'pool_kernel_size':(2,2)}
               }

dense_params  = {'0':{'nodes':32,
                      'activation':'relu'},
                 '1':{'nodes':64,
                      'activation':'relu'}
                 }



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
model = mac.model_architecture_constructor(imdim,conv_layers,dense_layers,
                                           classes,conv_params,dense_params)


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

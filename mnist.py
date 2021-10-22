from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras import models  
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Activation  
from keras_visualizer import visualizer 
from keras import layers 

import matrixServer

mnist = keras.datasets.mnist 
class_names = ['1','2','3','4','5','6','7','8','9','0']


# TODO: load data from the mnist dataset

# TODO: normalize the data (it goes from 0 to 255 right now)



# TODO: make a sequential keras model with the following 4 layers
  # 1. Flatten to 28x28
  # 2+3. Two relu layers of size 128
  # 4. Output with softmax activation

# TODO: compile the model optimizer='adam',
  #           loss='sparse_categorical_crossentropy',
  #           metrics=['accuracy'])

# TODO: fit the model with 10 epochs



# TODO: evaluate model against training data

# TODO: print accuracy


def gotMatrix(matrix):

  # What number did the user just draw!?!?!?

  # Optional: Use matplotlib to plot the matrix the user drew

  # TODO: make a prediction based on the matrix using the already trained model

  # TODO: print AND return the prediction

  pass
  

matrixServer.subscribe(gotMatrix, True)

matrixServer.start(28, 28, 10)



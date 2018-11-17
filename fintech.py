import keras
import tensorflow as tf
import numpy as np
import tkinter
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense

def build_model(input_size, output_size):
    model = Sequential()
    model.add(Dense(256, input_shape=(input_size,), activation='softmax'))
    model.add(Dense(units=output_size , activation='softmax'))
    model.compile(optimizer=Adam(), loss='mse')

    return model











import keras
import tensorflow as tf
import numpy as np
import tkinter
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense


class FinanceBot:
    def __init__(self, o):
        self.model = Sequential()
        self.build_model(7, o)

    def build_model(self, input_size, output_size):
        # self.model = Sequential()
        self.model.add(Dense(256, input_shape=(input_size,), activation='softmax'))
        self.model.add(Dense(units=output_size , activation='softmax'))
        self.model.compile(optimizer=Adam(), loss='mse')

        return self.model











import keras
import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense


day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
week1=[31.16,6.02,8.26,0,12.17,14.87,3.55]
week2=[24.71,10.79,22.55,220.45,16.85,0,0]
week3=[32.34,37.71,233.33,38.87,10.8,117.23,0]
week4=[32.55,145.31,10.8,22.35,18.2,23.84,0]
week5=[78.62,152.04,25.2,0,15.83,2.6,7.13]
week6=[96.45,17.38,39.35,53.27,65.33,172.39,19.4]
data=[week1,week2,week3,week4,week5,week6]





class FinanceBot:
  
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Dense(256, input_shape=(7,), activation='softmax'))
        model.add(Dense(units=7, activation='softmax'))
        model.compile(optimizer=Adam(), loss='mse')
        return model

    def train_neural(self, training_data):
        sample = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
        label = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))
        self.model.fit(sample, label, epochs=10)
        return self.model

    def get_stats(self):

        pass


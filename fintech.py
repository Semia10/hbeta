import keras
import tensorflow as tf
import numpy as np
import tkinter
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dense

week1 = [76.03, 31.16, 6.02, 8.26, 0, 12.17, 14.87, 3.55]
week2 = [295.35, 24.71, 10.79, 22.55, 220.45, 16.85, 0, 0]
week3 = [470.28, 32.34, 37.71, 233.33, 38.87, 10.8, 117.23, 0]
week4 = [253.05, 32.55, 145.31, 10.8, 22.35, 18.2, 23.84, 0]
week5 = [281.42, 78.62, 152.04, 25.2, 0, 15.83, 2.6, 7.13]
week6 = [463.57, 96.45, 17.38, 39.35, 53.27, 65.33, 172.39, 19.4]
week7 = [114.34, 0, 46.62, 26.49, 7.35, 17.41, 6.63, 9.84]
week8 = [261.41, 37.22, 4.99, 10.29, 17.49, 177.25, 14.17, 0]
data = [week1, week2, week3, week4, week5, week6, week7, week8]

new_array = data.copy()


class FinanceBot:
    def __init__(self):
        self.model = Sequential()
        self.build_model(7, 7)

    def build_model(self, input_size, output_size):
        # self.model = Sequential()
        self.model.add(Dense(256, input_shape=(input_size,), activation='softmax'))
        self.model.add(Dense(units=output_size, activation='softmax'))
        self.model.compile(optimizer=Adam(), loss='mse')

        return self.model

    def train(self, data):
        for i in data:
            total = 0
            for k in i:
                if total == 0:
                    total = k
                else:
                    k /= total
        return self.model

    def get_stats(self):
        pass


if __name__ == "__main__":
    bot = FinanceBot()
    bot.train(data)

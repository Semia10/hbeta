import keras
import tensorflow as tf
import numpy as np
import tkinter
from keras.models import Sequential
from keras.optimizers import Adagrad
from keras.layers import Dense

week1 = [76.03, 31.16, 6.02, 8.26, 0, 12.17, 14.87, 3.55]
week2 = [295.35, 24.71, 10.79, 22.55, 220.45, 16.85, 0, 0]
week3 = [470.28, 32.34, 37.71, 233.33, 38.87, 10.8, 117.23, 0]
week4 = [253.05, 32.55, 145.31, 10.8, 22.35, 18.2, 23.84, 0]
week5 = [281.42, 78.62, 152.04, 25.2, 0, 15.83, 2.6, 7.13]
week6 = [463.57, 96.45, 17.38, 39.35, 53.27, 65.33, 172.39, 19.4]
week7 = [114.34, 0, 46.62, 26.49, 7.35, 17.41, 6.63, 9.84]
week8 = [261.41, 37.22, 4.99, 10.29, 17.49, 177.25, 14.17, 0]
week9 = [80.09, 0, 26.75, 5.78, 15.38, 24.83, 7.35, 0]
week10 = [266.66, 111.48, 17.67, 15.27, 7.77, 24.38, 0, 90.09]
week11 = [58.04, 0, 0, 7.96, 0, 25.05, 25.03, 0]
week12 = [146.56, 37.77, 0, 32.25, 44.9, 18.71, 12.93, 0]
week13 = [101.49, 0, 15.19, 0, 13.16, 19.71, 26.66, 26.77]
week14 = [110.52, 0, 13.63, 19.18, 35.02, 20.17, 22.52, 0]
week15 = [86.34, 0, 25.55, 5.13, 36.29, 13.52, 0, 5.85]
data = [week1, week2, week3, week4, week5, week6, week7, week8, week9, week10, week11, week12, week13, week14, week15]


class FinanceBot:
    def __init__(self):
        self.model = Sequential()
        self.build_model(8, 7)

    def build_model(self, input_size, output_size):
        # self.model = Sequential()
        self.model.add(Dense(24, input_shape=(input_size,), activation='softmax'))
        self.model.add(Dense(units=output_size, activation='softmax'))
        self.model.compile(optimizer=Adagrad(), loss='mse')
        return self.model

    def training_data(self, input_data):
        training_data = []
        for i in data:
            output_data = []
            total = 0
            for k in i:
                if total == 0:
                    total = k
                else:
                    k /= total
                    output_data.append(k)
            training_data.append([i, output_data])
        return training_data
    
    def train_neural(self, training_data):
        sample = np.array([i[0] for i in training_data]).reshape(-1, len(training_data[0][0]))
        label = np.array([i[1] for i in training_data]).reshape(-1, len(training_data[0][1]))
        self.model.fit(sample, label, epochs=100, shuffle=True)
        return self.model

    def get_stats(self, your_data):
        stat = self.model.predict(your_data.reshape(-1, len(your_data)))
        return stat

if __name__ == "__main__":
    bot = FinanceBot()
    training_data = bot.training_data(data)
    bot.train_neural(training_data)
    your_data = np.array([502, 5, 34, 183, 125, 43, 83, 29])
    predicted_data = bot.get_stats(your_data)
    print(predicted_data[0])


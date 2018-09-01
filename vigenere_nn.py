import tensorflow as tf
from tensorflow import keras
import numpy as np
import data_generator
import string
import random
import statistics

train_data, train_labels = data_generator.generate_data(100)
test_data, test_labels = data_generator.generate_data(10)

model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(len(statistics.stats_funcs),)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.softmax)
])

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='mean_absolute_error',
              metrics=['accuracy'])


model.fit(train_data, train_labels, epochs=5)

test_loss, test_acc = model.evaluate(test_data, test_labels)

print("test accuracy", test_acc)

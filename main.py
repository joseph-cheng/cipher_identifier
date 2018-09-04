print("Importing...")
from tensorflow import keras
import tensorflow as tf
import numpy as np
import data_generator
import string
import random
import statistics
import os

# Setup saving checkpoints
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                 save_weights_only=True,
                                                 verbose=1)
# Creates untrained model
def create_model():
    print("Creating model...")
    model = keras.Sequential([
        keras.layers.Dense(32, input_shape=(len(statistics.stats_funcs),)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(len(data_generator.config), activation=tf.nn.softmax)
    ])

    print("Compiling model...")
    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

#Takes in a model and ciphertext and asks the neural network what cipher it is
def predict(m, ct):
    test = np.array([func(ct) for func in statistics.stats_funcs])
    test = (np.expand_dims(test,0))
    prediction = m.predict(test)[0]
    for probability in sorted(zip(prediction, range(len(data_generator.config.values()))), key=lambda x: x[0], reverse=True):
        print(data_generator.reverse_config[probability[1]], probability[0])
    

print("Generating data...")
data_generator.generate_data(1000, "data/train_data.dat", "data/train_labels.dat")
data_generator.generate_data(100, "data/test_data.dat", "data/test_labels.dat")

#Load in data
train_data = np.load("data/train_data.dat")
train_labels = np.load("data/train_labels.dat")
test_data = np.load("data/test_data.dat")
test_labels = np.load("data/test_labels.dat")

model = create_model()
print("Training model...")
model.fit(train_data, train_labels, epochs=5,
          callbacks = [cp_callback])
          
model.load_weights(checkpoint_path)

print("Testing model...")
test_loss, test_acc = model.evaluate(test_data, test_labels)

print("test accuracy", test_acc)

while True:
    ct = input("Enter ciphertext to identify: ")
    ct = "".join([char.upper() for char in ct if char.isalpha()])
    predict(model, ct)

print("Importing...")
from tensorflow import keras
import tensorflow as tf
import numpy as np
import data_generator
import string
import random
import statistics
import os

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)
cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path, 
                                                 save_weights_only=True,
                                                 verbose=1)

def create_model():
    print("Creating model...")
    model = keras.Sequential([
        keras.layers.Dense(32, input_shape=(len(statistics.stats_funcs),)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(2, activation=tf.nn.softmax)
    ])

    print("Compiling model...")
    model.compile(optimizer=tf.train.AdamOptimizer(),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    return model

print("Generating data...")
#train_data, train_labels = data_generator.generate_data(1000)
test_data, test_labels = data_generator.generate_data(100)

model = create_model()
print("Training model...")
#model.fit(train_data, train_labels, epochs=5,
#          validation_data = (test_data, test_labels),
#          callbacks = [cp_callback])
          
model.load_weights(checkpoint_path)

print("Testing model...")
test_loss, test_acc = model.evaluate(test_data, test_labels)

print("test accuracy", test_acc)

ct = 'DEYRBUGZWRVEFMYPEOARGTDHXMGWHRRRQRLGSZVEVVIESUZRTUOEHVRSSLLQVBCYWYHVRLOEUGVTOTGXDVQWUSBLJNHELFQARJLLBIIGKJAEGMQGUTGNQAQCENRYYVOAIKPNJGCYDRPWVFSOVQOTGKKIAWETPNICZKRZIXUSAWNYEUKXEZWANKIUEOMQHATZWWRWTSGNIGZGCZWYFZHDNHMGZKRZGINLOEOGJLRUNZDRTGKDRYABLROMHEAVDAECIFOYHKDVNFKTUKQFNZAIJEGWMRBSJNHELFQANKVNRUNGNKOILKVFHLFKDRTCOEGIEKVFGNMJUXLULXJSZLNZMEXKPCDGRVIYGNMYOMHKKSHKLOSGTRDGNUUMNKVINSVBZYUIHAUQAAPOBHYASVGFBLOBHZUNEHESHGNMZEUKLVJTTBQSJOOEEKBUKNAEJMAYNAEJMAYCEIHIVLOEEUZZGEBVKIWMZTJGVGKJTFFSAXBSRZPRATIELXVSAEQGVQZUAUGEAWETEGTNEKRFIWRUYEPEDVGIOEIYFAVNNHQGROKVKIQGLSOEXVRONXXTPAWHRXAVTZHVVIYSAEEIPNVZEIVEAQDALCMNXKIEOYPCAHROAUZGRXDXRFVWYODRYONKKICWYGNSWASASVXQVFIEERQAGTDZKECHLNGUPNBKAGDWFLVTUKNHRRCFOPRUAIBTQNSTOKVYEWOOJZPRECICOJRWSAOUCGAYDZVQNFALVTOVZZOKUCGGMIAJKUGVTVUWRNLNOABVLCEVATYSPNJNIGOYIELXVKBSCKKGZNETXVNLVRFICEOUSZWCJASLBBMEIUMVKMFFHTHXIYVXOKHGGACEAKAFVKRYDTFLOEEKERCOLCIMASSLLAVYUIKKKIFWJRRZWSZNEZAXUDLGVUVGNGTCHEIWZTUKYHKYTZRRBXOOJCMQKGLNLXUEPDNYIAJSAIBEZZHSNITRBKRZGINOLSUUCYJREKWLRUVLYKKGUXDVDPJAAHGNMZZNEIXWFAHNZGNVGIAEEICJLTGEZHZNLVVWVXAHRENRKRBVWVNQLDNTLFNKHRVWHYNEFZMQGCAPZIZANHGSIXKZHVWLVWCEFLIYRUUKLXVKHCHTVVTMPCDRNFKIGNQAQOCRQLRDW'

test = test_data[0]
print(test.shape)
test = (np.expand_dims(test,0))
prediction = model.predict(test)
print(prediction)

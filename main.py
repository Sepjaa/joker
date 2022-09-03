# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:40:17 2022

@author: Jaakko
"""

import tensorflow as tf
from tensorflow import keras

import models
import config

EPOCHS = 20
PREFIX = "{}-{}-{}".format(config.EMBEDDING_DIM, config.RNN_UNITS, config.LAYERS)

ids_dataset = tf.data.Dataset.from_tensor_slices(config.all_ids)
seq_length = 100
sequences = ids_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text


dataset = sequences.map(split_input_target)

# Batch size
BATCH_SIZE = 128

# Buffer size to shuffle the dataset
# (TF data is designed to work with possibly infinite sequences,
# so it doesn't attempt to shuffle the entire sequence in memory. Instead,
# it maintains a buffer in which it shuffles elements).
BUFFER_SIZE = 10000

dataset = (
    dataset
        .shuffle(BUFFER_SIZE)
        .batch(BATCH_SIZE, drop_remainder=True)
        .prefetch(tf.data.experimental.AUTOTUNE))

model = models.create(config.vocab_size, config.EMBEDDING_DIM, config.RNN_UNITS, config.LAYERS)

class CustomCallback(keras.callbacks.Callback):

    def __init__(self, model):
        self.model = model

    def on_epoch_end(self, epoch, logs=None):
        self.model.save_weights("models/{}-chk-{}-{:.4f}".format(PREFIX, epoch, logs["loss"]))
        print("Saved epoch {} with loss {}".format(epoch, logs["loss"]))

    def on_train_end(self, logs=None):
        self.model.save_weights("models/{}-end-{:.4f}".format(PREFIX, logs["loss"]))
        print("Saved end with loss {}".format(logs["loss"]))

history = model.fit(dataset, epochs=EPOCHS, callbacks=[CustomCallback(model)])


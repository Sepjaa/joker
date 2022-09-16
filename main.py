# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:40:17 2022

@author: Jaakko
"""

import tensorflow as tf
from tensorflow import keras

import models
import config

PREFIX = "{}-{}".format(config.EMBEDDING_DIM, config.RNN_UNITS)

ids_dataset = tf.data.Dataset.from_tensor_slices(config.all_ids)
seq_length = 100
sequences = ids_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(sequence):
    input_text = sequence[:-1]
    target_text = sequence[1:]
    return input_text, target_text


dataset = sequences.map(split_input_target)



dataset = (
    dataset
        .shuffle(config.BUFFER_SIZE)
        .batch(config.BATCH_SIZE, drop_remainder=True)
        .prefetch(tf.data.experimental.AUTOTUNE))

model = models.create(config.vocab_size, config.EMBEDDING_DIM, config.RNN_UNITS, config.DROPOUT)

class CustomCallback(keras.callbacks.Callback):

    def __init__(self, model):
        self.model = model

    def on_epoch_end(self, epoch, logs=None):
        if epoch % config.MODEL_CHECKPOINT_INTERVAL_EPOCHS == 0:
            self.model.save_weights("{}/{}-chk-{}-{:.4f}".format(config.MODEL_FOLDER, PREFIX, epoch, logs["loss"]))
            print("Saved epoch {} with loss {}".format(epoch, logs["loss"]))

    def on_train_end(self, logs=None):
        self.model.save_weights("{}/{}-end-{:.4f}".format(config.MODEL_FOLDER, PREFIX, logs["loss"]))
        print("Saved end with loss {}".format(logs["loss"]))

history = model.fit(dataset, epochs=config.EPOCHS, callbacks=[CustomCallback(model)])


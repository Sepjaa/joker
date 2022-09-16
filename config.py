import tensorflow as tf
import csv
import numpy as np

# Technical parameters
# Filepath where model checkpoints are saved, default saves to relative directory
MODEL_FOLDER = "models"
# Unique character not in dataset to distinguish end of joke in training data
END_OF_JOKE_CHARACTER = "∅"

# Training parameters
# How many epochs are ran in training
EPOCHS = 256
# Save model checkpoint every N epochs
MODEL_CHECKPOINT_INTERVAL_EPOCHS = 5
# Batch size
BATCH_SIZE = 64
# Buffer size to shuffle the dataset
BUFFER_SIZE = 100000
# Learning rate for optimizer
LEARNING_RATE = tf.keras.optimizers.schedules.ExponentialDecay(
        initial_learning_rate=0.002,
        decay_steps=15000,
        decay_rate=0.95)
# Optimizer instance, adamax is used as a default because of good performance in recurrent networks
OPTIMIZER = tf.keras.optimizers.Adamax(
    learning_rate=LEARNING_RATE,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    name='Adamax',
    )

# Model parameters
# The embedding dimension
EMBEDDING_DIM = 128
# Number of RNN units
RNN_UNITS = 2048
# Dropout after RNN layer
DROPOUT = 0.2

jokes = []
with open("shortjokes.csv", newline="") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    next(spamreader, None)
    for row in spamreader:
        jokes.append(row[1])
data = []
for joke in jokes:
    padded = "".join((joke, END_OF_JOKE_CHARACTER))
    data.append(padded)
data = np.array(data);
text = "".join(str(joke) for joke in data)
vocab = sorted(set(text))
print(f'{len(vocab)} unique characters')

chars = tf.strings.unicode_split(data, input_encoding='UTF-8')
ids_from_chars = tf.keras.layers.StringLookup(
    vocabulary=list(vocab), mask_token=None)
ids = ids_from_chars(chars)
chars_from_ids = tf.keras.layers.StringLookup(
    vocabulary=ids_from_chars.get_vocabulary(), invert=True, mask_token=None)
chars = chars_from_ids(ids)


def text_from_ids(ids):
    return tf.strings.reduce_join(chars_from_ids(ids), axis=-1)


all_ids = ids_from_chars(tf.strings.unicode_split(text, 'UTF-8'))
ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)

# Length of the vocabulary in StringLookup Layer
vocab_size = len(ids_from_chars.get_vocabulary())

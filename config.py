import tensorflow as tf
import csv
import numpy as np
MODEL_FOLDER = "Z:/models"
END_OF_JOKE_CHARACTER = "∅"
# The embedding dimension
EMBEDDING_DIM = 256
# Number of RNN units
RNN_UNITS = 2048

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

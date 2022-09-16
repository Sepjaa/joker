import models
import time
import config
import tensorflow as tf
# How many jokes to produce
jokes = 200
# How the jokes should start
feed = "Knock knock. Who's there? "
# Spiciness
temperature = 0.2
# Model filename without the .index or .data suffix
model_filename = "128-2048-end-0.6664"

file = "{}/{}".format(config.MODEL_FOLDER, model_filename)

model = models.create(config.vocab_size, config.EMBEDDING_DIM, config.RNN_UNITS, config.DROPOUT)

model.load_weights(file)

one_step_model = models.OneStep(model, config.chars_from_ids, config.ids_from_chars, temperature)

start = time.time()
states = None
end_char = tf.constant([config.END_OF_JOKE_CHARACTER])
next_char = tf.constant([feed])

for i in range(jokes):
    joke = [next_char]
    i = 0
    while next_char.numpy() != end_char.numpy():
        i += 1
        if i > 100:
            break
        next_char, states = one_step_model.generate_one_step(next_char, states=states)
        if next_char.numpy() != end_char.numpy():
            joke.append(next_char)
    joke = tf.strings.join(joke)
    print(joke[0].numpy().decode('utf-8'))
    next_char = tf.constant([feed])


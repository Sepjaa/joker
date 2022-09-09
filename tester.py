import models
import time
import config
import tensorflow as tf

jokes = 10
feed = "You"
temperature = 0.1
file = "{}/{}".format(config.MODEL_FOLDER, "256-2048-chk-105-0.5367")

# model = tf.saved_model.load("models/2048-chk-5-1.1497799158096313")
model = models.create(config.vocab_size, config.EMBEDDING_DIM, config.RNN_UNITS)

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
        if(i > 500):
            break;
        next_char, states = one_step_model.generate_one_step(next_char, states=states)
        if next_char.numpy() != end_char.numpy():
            joke.append(next_char)
    joke = tf.strings.join(joke)
    print(joke[0].numpy().decode('utf-8'))
    next_char = tf.constant([feed])

end = time.time()
# print(result[0].numpy().decode('utf-8'), '\n\n' + '_' * 80)
print('\nRun time:', end - start)

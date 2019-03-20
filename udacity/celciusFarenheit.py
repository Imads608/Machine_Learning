import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
def algorithm():
    tf.logging.set_verbosity(tf.logging.ERROR)
    celcius_q = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
    farenheit_a = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

    network = tf.keras.layers.Dense(units=1, input_shape=[1])
    model = tf.keras.Sequential([network])

    model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.1))
    history = model.fit(celcius_q, farenheit_a, epochs=500, verbose=False)

    plt.xlabel("Epoch Number")
    plt.ylabel("Loss Magnitude")
    plt.plot(history.history['loss'])
    plt.show()
    print(model.predict([100.0]))
    print("Internal Variables: {}".format(network.get_weights()))

if __name__ == "__main__":
    algorithm()
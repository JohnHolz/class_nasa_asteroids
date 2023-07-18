import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential

## optimizer
rms = "rmsprop"
adam = "adam"
SPC = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
CC = tf.keras.losses.CategoricalCrossentropy()
BC = "binary_crossentropy"
MSE = "mse"
SCC = "sparse_categorical_crossentropy"
softmax = "softmax"


def multi_layer_model(
    n_layers=[16, 8],
    loss="binary_crossentropy",
    optimizer="adam",
    last_layer_activation="sigmoid",
):
    tf_model = Sequential()
    tf_model.add(Dense(10, activation="relu", input_shape=(38,)))
    for i in n_layers:
        tf_model.add(Dense(i, activation="relu"))
    tf_model.add(Dense(1, activation=last_layer_activation))
    tf_model.compile(
        loss=loss,
        optimizer=optimizer,
        metrics=[tf.keras.metrics.Precision(), "accuracy"],
    )
    return tf_model

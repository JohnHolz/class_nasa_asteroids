import tensorflow as tf

## optimizer
rms='rmsprop'
adam='adam'

## loss
SPC = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
CC = tf.keras.losses.CategoricalCrossentropy()
BC = 'binary_crossentropy'
MSE = 'mse'
SCC = 'sparse_categorical_crossentropy'

## last layer
softmax = 'softmax'
sigmoid = 'sigmoid'

def model_3():
    model_3 = tf.keras.Sequential()
    model_3.add(tf.keras.layers.Dense(8, activation='relu', input_shape=(43,)))
    model_3.add(tf.keras.layers.Dense(16, activation='relu'))
    model_3.add(tf.keras.layers.Dense(10, activation='relu'))
    model_3.add(tf.keras.layers.Dense(1, activation='sigmoid'))#sigmoid
    model_3.compile(loss=BC, optimizer=adam, metrics=[tf.keras.metrics.Precision(),'accuracy'])
    return model_3
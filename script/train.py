"""
Module for training the neural network model.
"""
from tensorflow.keras.optimizers import Adam


def train_model(model, x_train, y_train, epochs=15, batch_size=128, callbacks=None):
    model.compile(loss="categorical_crossentropy",
                  optimizer=Adam(learning_rate=0.01),
                  metrics=["accuracy"])
    history = model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_split=0.1,
              callbacks=callbacks)
    return history

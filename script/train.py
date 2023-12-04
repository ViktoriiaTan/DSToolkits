"""
Module for training the neural network model.
"""


def train_model(model, x_train, y_train, epochs=15, batch_size=128):
    model.compile(loss="categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              validation_split=0.1)

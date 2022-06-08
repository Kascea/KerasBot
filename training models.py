import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

image_size = (256, 256)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "KerasImages",
    labels="inferred",
    validation_split=0.2,
    subset="training",
    seed=1337,
    shuffle=True,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "KerasImages",
    labels="inferred",
    validation_split=0.2,
    subset="validation",
    seed=1337,
    shuffle=True,
    image_size=image_size,
    batch_size=batch_size,
)


model = keras.Sequential([
    keras.layers
])

epochs = 50
callbacks = [
    keras.callbacks.ModelCheckpoint("save_at_{epoch}.h5"),
]
model.compile(
    optimizer=keras.optimizers.Adam(1e-3),
    loss="binary_crossentropy",
    metrics=["accuracy"],
)
model.fit(
    train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds,
)

model.save('trainedmodel')

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# モデル読み込み
model = tf.keras.models.load_model("dog_cat_model.h5")

# テストデータ
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    "dataset",
    target_size=(224, 224),
    batch_size=32,
    class_mode="binary",
    shuffle=False
)

# 評価
loss, accuracy = model.evaluate(test_generator)

print(f"正解率: {accuracy * 100:.2f}%")
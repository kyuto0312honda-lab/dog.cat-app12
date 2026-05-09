from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# モデル読み込み
model = tf.keras.models.load_model("dog_cat_model.h5")

# アップロードフォルダ
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_path = None

    if request.method == "POST":
        file = request.files["file"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # 画像読み込み
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = img_array / 255.0

            # 予測
            prediction = model.predict(img_array)[0][0]

            if prediction > 0.5:
                result = "犬"
            else:
                result = "猫"

            image_path = filepath

    return render_template(
        "index.html",
        result=result,
        image_path=image_path
    )

if __name__ == "__main__":
    app.run(debug=True)
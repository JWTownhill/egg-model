from fastai.vision.all import *
import os
from urllib.request import urlretrieve
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

model_path = Path("model.pkl")

try:
    learner = load_learner(model_path)
except FileNotFoundError:
    MODEL_URL = "https://egg-model.s3.eu-west-2.amazonaws.com/export.pkl"
    urlretrieve(MODEL_URL, "model.pkl")
    learner = load_learner(model_path)

print("Model loaded. Start serving...")


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


# img = PILImage.create(btn_upload.data[-1])
# pred, pred_idx, probs = learn.predict(img)
# lbl_pred.value = f'Prediction: {pred} egg; Probability: {probs[pred_idx]:.02f}'

if __name__ == "__main__":
    app.run()
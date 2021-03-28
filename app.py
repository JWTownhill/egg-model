from fastai.vision.all import *
import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

path = Path()
learn = load_learner(path / "model/export.pkl")


@app.route("/")
def home():
    return "Hello world"

#img = PILImage.create(btn_upload.data[-1])
#pred, pred_idx, probs = learn.predict(img)
#lbl_pred.value = f'Prediction: {pred} egg; Probability: {probs[pred_idx]:.02f}'

if __name__ == "__main__":
    app.run()
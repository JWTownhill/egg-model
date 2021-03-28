from fastai.vision.all import *
from flask import Flask

app = Flask(__name__)

path = Path()
learn = load_learner(path / "model/export.pkl")


@app.route("/")
def home():
    return "Hello world"


if __name__ == "__main__":
    app.run()
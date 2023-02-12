from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

import tensorflow as tf
model = tf.keras.models.load_model('Integer Identification/my_mnist_model')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request
import numpy as np
import pickle
import json

app = Flask(__name__)

@app.route("/")
def home():
    model = pickle.load(open('model.pk', 'rb'))  # loading saved model
    x = np.array([5.4, 3.2, 5.4, 2.8])
    x = x.reshape(1, 4)
    p = model.predict(x)
    d = {'Predicted_class': str(p)}
    return jsonify(d)

@app.route("/json")  # /json
def json():
    data = [{'name': 'Yourname', 'Surname': 'Yoursurname'}, {'Id': '1'}]
    return jsonify(data)

@app.route('/iris/<string:sample>', methods=['GET']) # /iris/python
def getData(sample):
    return sample

@app.route('/predict', methods=['GET'])  # /predict?key1=value1&amp;key2=value2
def predict():
    slength = request.args.get('sepallength')
    swidth = request.args.get('sepalwidth')
    plength = request.args.get('petallength')
    pwidth = request.args.get('petalwidth')

    model = pickle.load(open('model.pk', 'rb'))
    x = np.array([slength, swidth, plength, pwidth])
    x = x.reshape(1, 4)
    p = model.predict(x)
    d = [{'Predicted_class': str(p)}]
    return jsonify(d)


if __name__ == "__main__":
    app.run()
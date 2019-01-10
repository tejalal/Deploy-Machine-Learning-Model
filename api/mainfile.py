from flask import Flask, jsonify, request
import numpy as np
import pickle
import json

app = Flask(__name__)
 
@app.route("/")
def home():
    model = pickle.load(open('model.pk', 'rb'))
    x = np.array([5.4,3.2,5.4,2.8])
    x=x.reshape(1,4)
    p=model.predict(x)
    d = [{'Predicted_class':str(p)}]
    #tojso=json.dumps(d)
    #tostring = json.loads(tojso)
    return jsonify(d)
 

@app.route("/json") # /json
def json():
    data=[{'name':'Tejalal', 'Surname':'Choudhary'}, {'Id':'1'}]
    return jsonify(data)


@app.route('/iris/<string:sample>', methods=['GET']) # /iris/any-string
def getData(sample):
    return sample

@app.route('/predict', methods=['GET']) # /predict?key1=das&&key2=dsadas
def predict():
    slength=request.args.get('sepallength')
    swidth=request.args.get('sepalwidth')
    plength=request.args.get('petallength')
    pwidth=request.args.get('petalwidth')

    model = pickle.load(open('model.pk', 'rb'))
    x = np.array([slength,swidth,plength,pwidth])
    x=x.reshape(1,4)
    p=model.predict(x)
    d = [{'Predicted_class':str(p)}]
    return jsonify(d)

if __name__ == "__main__":
    app.run()



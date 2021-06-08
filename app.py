# -*- coding: utf-8 -*-
"""fapp

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f26E8d4GTkFvdmeL3t6WSIa5KHYqUS3U
"""

import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["POST"])
def predict():
    if request.method == "POST":
        message = request.form['message']
    	data = [message]
    	vect = cv.transform(data).toarray()
    	my_prediction = classifier.predict(vect)   
        return render_template('prediction.html',prediction=my_prediction)

if __name__ == "__main__":
    app.run(debug=True)

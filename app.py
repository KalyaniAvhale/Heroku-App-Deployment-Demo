# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 11:32:56 2021

@author: kalyani
Web app using flask
"""

from flask import Flask,render_template,url_for,request,jsonify
import pickle
import numpy as np

#create instance of flask app
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# @app.route that Flask uses to connect URL endpoints with code contained in functions. T
# the argument to @app.route defines the URL’s path component, 
# which is the root path ("/") in this case.

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    
    return render_template("index.html", prediction_text="Salary Should be $ {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)
    



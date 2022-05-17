from flask import Flask, jsonify,request
import pickle
import pandas as pd

app = Flask(__name__)

IRIS_CLASSES = ['setosa', 'versicolor', 'virginica']

with open('iris_pipe.pkl', 'rb') as f:
    model_iris = pickle.load(f)

LABEL = ['Not Survived', 'Survived']
kolumns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
with open("titanic_pipe.pkl", "rb") as f:
    model_titanic = pickle.load(f)


@app.route("/titanic",methods=['GET','POST'])
def titanic_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [data['Passanger_Class'],
                    data['Gender'],
                    data['Age'],
                    data['Sibling_spouse'],
                    data['Parent_children'],
                    data['Fare']]
        new_data = pd.DataFrame([new_data],columns=kolumns)
        res = model_titanic.predict(new_data)
        response = {'code': 200, 'status': 'OK', 
                    'result': {'prediction': str(res[0]),
                                'classes': LABEL[res[0]]}}
        return jsonify(response)
    return "Silahkan gunakan method post untuk mengakses model titanic"





@app.route("/")
def home_page():
    return "<h1>Backend Pemodelan Iris & TIitanic</h1>"


@app.route("/iris",methods=["GET",'POST'])
def iris_inference():
    if request.method == 'POST':
        data = request.json
        new_data = [data['sl'],data['sw'],data['pl'],data['pw']]
        res = model_iris.predict([new_data])
        response = {'code': 200, 'status': 'OK', 
                    'result': {'prediction': str(res[0]),
                               'classes': IRIS_CLASSES[res[0]]}}
        return jsonify(response)
    return "silahkan gunakan method post untuk mengakses model iris"



app.run(debug=True)
from flask import Flask, jsonify,request

app = Flask(__name__)


biodata = {'name': 'Farhan Zahirsyah',
           'age': 23,
           'pekerjaan': 'Data Scientist'}

@app.route("/")
def home_page():
    return jsonify(biodata)


@app.route("/change",methods=['POST'])
def change_biodata():
    global biodata
    data = request.json
    biodata['name'] = data['name']
    biodata['age'] = data['age']
    biodata['pekerjaan'] = data['pekerjaan']
    return 'Data telah diubah'



app.run(debug=True)
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Flask app after 2 years!!'


@app.route('/json')
def return_json():
    data = {
        'msg': 'json\'ed the data',
        'status': '200 success!!'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

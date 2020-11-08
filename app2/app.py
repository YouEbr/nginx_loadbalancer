import flask

app1 = flask.Flask(__name__)


@app1.route('/')
def hello_world():
    return 'This is App 2 :) '


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
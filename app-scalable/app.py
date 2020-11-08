import flask
import socket

app1 = flask.Flask(__name__)


@app1.route('/')
def hello_world():
    hostname, ip = get_hostname_and_ip()
    return 'This  web application is running on host:\"{}\" with ip:\"{}\"'.format(hostname, ip)


def get_hostname_and_ip():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return hostname, ip


if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')

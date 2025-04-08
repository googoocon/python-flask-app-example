from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(status='ok'), 200

@app.route('/version', methods=['GET'])
def version():
    return jsonify(version='1.0.0'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
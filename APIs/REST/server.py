from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/sumar', methods=['GET'])
def sumar():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return jsonify({"resultado": a + b})

if __name__ == '__main__':
    app.run(debug=True)

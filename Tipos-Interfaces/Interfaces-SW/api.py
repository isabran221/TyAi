from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    return jsonify({"mensaje": "Hola, esta es una API"})

if __name__ == '__main__':
    app.run(debug=True)

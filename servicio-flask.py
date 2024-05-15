from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/factorial/<int:n>', methods=['GET'])
def get_factorial(n):
    if n < 0:
        return jsonify({"error": "No se puede calcular el factorial de un número negativo"}), 400
    else:
        return jsonify({"factorial": factorial(n)}), 200

if __name__ == '__main__':
    app.run(debug=True)
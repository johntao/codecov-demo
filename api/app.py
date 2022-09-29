from flask import (
    Flask,
    request,
)

from calculator import Calculator

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add(): # pragma: no cover
    return operation('add', 2)

@app.route('/api/subtract', methods=['POST'])
def subtract(): # pragma: no cover
    return operation('subtract', 2)

@app.route('/api/multiply', methods=['POST'])
def multiply(): # pragma: no cover
    return operation('multiply', 2)

@app.route('/api/divide', methods=['POST'])
def divide(): # pragma: no cover
    return operation('divide', 2)

def operation(method, num_factors): # pragma: no cover
    factors = []
    if num_factors == 2:
        factors.append(float(request.json.get('x')))
        factors.append(float(request.json.get('y')))

    return str(getattr(Calculator, method)(*factors))


app.run(host='0.0.0.0', port=8080)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter  

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = "\n".join(str(i) for i in range(parameter)) + "\n"
    return numbers 

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2
        elif operation == '%':
            result = num1 % num2
        else:
            return "Error: Unsupported operation"
        return str(result) 
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"  

if __name__ == '__main__':
    app.run(port=5555, debug=True)

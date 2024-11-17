#1

import json

from flask import Flask, Response

app = Flask(__name__)
@app.route('/prime_number/<number1>')
def prime_check(number1):
    try:
        number1 = float(number1)
        if number1 > 1:
            for i in range(2, int(number1 / 2) + 1):
                if (number1 % i) == 0:
                    primecheck=f"{number1} is not a prime number"
                    break
                else:
                    primecheck=f"{number1} is a prime number"
        else:
            primecheck=f"{number1} is not a prime number"

        response = {
            "primecheck" : primecheck,
            "status" : 200
        }
        return response

    except ValueError:
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
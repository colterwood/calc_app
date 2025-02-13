from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Deine Calculator function
class Calculator(Resource):
    def get(self, operation):
        try:
            num1 = float(request.args.get("num1"))
            num2 = float(request.args.get("num2"))

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    return {"error": "Cannot divide by zero"}, 400
                result = num1 / num2
            else:
                return {"error": "Invalid operation"}, 400

            return {"operation": operation, "result": result}, 200
        except (TypeError, ValueError):
            return {"error": "Invalid input. Provide valid numbers."}, 400


# Define routes
api.add_resource(Calculator, "/calc/<string:operation>")

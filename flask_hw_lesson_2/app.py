from functools import wraps

from flask import Flask, request
from flask_restful import Api, Resource, reqparse, marshal_with, fields
import json

app = Flask(__name__)
api = Api(app)

companies_list = ["Coca-cola", "Amazon", "Apple"]

# Reqparser. With different location.
# Budle_erroes show all errors
parser_companies = reqparse.RequestParser(bundle_errors=True)
parser_companies.add_argument("page", "name", type=str, help="enter desired page",
                              location=["form", "headers", "cookies", "fields", "args"])
parser_copy = parser_companies.copy()
parser_replace = parser_companies.replace_argument("data", type=str, location=json, required=True)
parser_remove_arg = parser_companies.remove_argument("page")


# Custom type
class Upper(fields.Raw):
    def format(self, value):
        return value.upper()


# Nested structure.
nested_family_structure = {
    "father": fields.String,
    "mother": fields.String
}

# Custom structure.
structure_fish = {
    "name": Upper,
    "parameters": {"size": fields.List(fields.String),
                   "weight": fields.Integer
                   },
    "family": fields.Nested(nested_family_structure)
}


def decorator(f):
    @wraps(f)
    def decoration(*args, **kwargs):
        print("Hello!")
        return f(*args, **kwargs)
    return decoration


class Fish(Resource):
    def __init__(self, name, size, weight):
        self.name = name
        self.size = size
        self.weight = weight
        self.family = {
            "father": "Tom",
            "mother": "Kate"
        }


class GetFish(Resource):
    # Decorator for all methods. For certain use {"get":"decorator"}
    # For loggin, session (if its expired)
    # method_decorators = [decorator]

    @marshal_with(structure_fish)
    def get(self):
        fish = Fish("Carp", ["22cm", "5cm"], 300)
        return fish


class Hello(Resource):
    def get(self):
        return {"hello": "world"}, 200, {"custom_header": "emm"}

    def post(self):
        return "bla bla", 201


parser_companies = reqparse.RequestParser(bundle_errors=True)
parser_companies.add_argument("page", "name", type=str, help="enter desired page",
                              location="args")


class Companies(Resource):
    def get(self):
        args = parser_companies.parse_args()

        print(args)
        response = dict()
        for i, elem in enumerate(companies_list):
            response[i + 1] = elem
        return response

    def post(self, value):
        companies_list.append(value)
        return "Successful"

    def put(self):
        data = json.loads(request.data)
        company = data.get("company")
        position = data.get("position") - 1

        companies_list.remove(company)
        companies_list.insert(position, company)
        return "Successful"

    def delete(self, value):
        companies_list.remove(value)
        return "Successful"


api.add_resource(Hello, "/")
api.add_resource(Companies, "/companies", "/companies/<value>")
api.add_resource(GetFish, "/fish")

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, render_template, request
import json

vegetables_blueprint = Blueprint("vegetables_blueprint", __name__, template_folder="templates")


@vegetables_blueprint.route("/vegetables")
@vegetables_blueprint.route("/vegetables/<string:value>", methods=["POST", "DELETE"])
def vegetables(value=None):
    if request.method == "POST":
        add_vegetables(value)
        return "New vegetable successfully added"
    elif request.method == "DELETE":
        delete_vegetables(value)
        return f"Vegetable {value} successfully deleted"
    else:
        return get_vegetables()


def get_vegetables():
    with open("./db_grocery/vegetables.json", 'r') as f:
        file_data = json.load(f)
        list_of_vegetables = file_data['vegetables']
    return render_template("vegetables.html", list_of_vegetables=list_of_vegetables)


def to_json(file_data, filename="./db_grocery/vegetables.json"):
    with open(filename, 'w') as f:
        json.dump(file_data, f)


def add_vegetables(value):
    with open("./db_grocery/vegetables.json", 'r') as f:
        file_data = json.load(f)
        file_data["vegetables"].append(value)
    to_json(file_data)


def delete_vegetables(value):
    try:
        with open("./db_grocery/vegetables.json", 'r') as f:
            file_data = json.load(f)
            file_data["vegetables"].remove(value)
        to_json(file_data)
    except ValueError:
        print("There is no such value in database.")

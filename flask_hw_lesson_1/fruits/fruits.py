from flask import Blueprint, render_template, request
import json
import os
from werkzeug.utils import secure_filename

fruits_blueprint = Blueprint("fruits_blueprint", __name__, template_folder="templates", static_folder="fruit_photos")


@fruits_blueprint.route("/fruits")
@fruits_blueprint.route("/fruits/<string:value>", methods=["POST", "DELETE"])
def fruits(value=None):
    if request.method == "POST":
        add_fruit(value)
        return "Fruit successfully added"
    elif request.method == "DELETE":
        delete_fruit(value)
        return f"Fruit {value} successfully deleted"
    else:
        return get_fruits()


@fruits_blueprint.route("/fruits", methods=["POST"])
def file_upload():
    if request.method == "POST":
        f = request.files['file']
        file_path = os.path.join("fruits/fruit_photos", secure_filename(f.filename))
        f.save(file_path)
        return "File uploaded!"


def show_photos():
    fruit_photos = os.listdir('./fruits/fruit_photos')
    fruit_photos = ['fruit_photos/' + file for file in fruit_photos]
    return fruit_photos


def get_fruits():
    with open("./db_grocery/fruits.json", 'r') as f:
        file_data = json.load(f)
        list_of_fruits = file_data['fruits']
    return render_template("fruits.html", list_of_fruits=list_of_fruits, fruit_photos=show_photos())


def to_json(file_data, filename="./db_grocery/fruits.json"):
    with open(filename, 'w') as f:
        json.dump(file_data, f)


def add_fruit(value):
    with open("./db_grocery/fruits.json", 'r') as f:
        file_data = json.load(f)
        file_data["fruits"].append(value)
    to_json(file_data)


def delete_fruit(value):
    try:
        with open("./db_grocery/fruits.json", 'r') as f:
            file_data = json.load(f)
            file_data["fruits"].remove(value)
        to_json(file_data)
    except ValueError:
        print("There is no such value in database.")


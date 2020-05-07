from flask import Flask
from .fruits.fruits import fruits_blueprint
from .vegetables.vegetables import vegetables_blueprint
from .main_page.main_page import main_page

app = Flask(__name__, static_folder='static')

app.register_blueprint(fruits_blueprint)
app.register_blueprint(vegetables_blueprint)
app.register_blueprint(main_page)

from flask import Blueprint, render_template, redirect, url_for


main_page = Blueprint("main_page", __name__, template_folder="templates")


@main_page.route("/")
def main():
    return render_template("main.html")


@main_page.route("/fruit")
def redirect_fruits_to_vegetables():
    return redirect(url_for('vegetables_blueprint.vegetables'))


@main_page.route("/error")
@main_page.errorhandler(403)
def error_403():
    return render_template("403.html"), 403

from flask import Blueprint, render_template, request, flash
from app import utils

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h3>Log out</h3>"

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password")
        password2 = request.form.get("password_confirm")
        print(username)
        print(utils.validate_username(username))
        print(utils.validate_password(password1))
        print(utils.confirm_password(password1, password2))

        if utils.validate_username(username) and utils.validate_password(password1) and utils.confirm_password(password1, password2):
            print("Account created")
            flash("Success: account created", category="success")

    return render_template("register.html")
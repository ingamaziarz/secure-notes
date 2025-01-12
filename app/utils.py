from flask import flash
import re
def validate_username(username):
    if len(username) < 3:
        flash("Username too short", category="error")
        return False
    return True
def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$'
    if not re.match(pattern, password):
        flash("Password too weak", category="error")
        return False
    entropy = 10
    threshold = 5
    if entropy < threshold:
        flash("Password too weak", category="error")
        return False
    return True
def confirm_password(password1, password2):
    if password1 != password2:
        flash("Passwords do not match", category="error")
        return False
    return True
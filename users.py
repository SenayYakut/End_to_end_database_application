from flask import Blueprint, render_template
from models import User

user_blueprint= Blueprint, render_template
from models import User
user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/<user_id>", methods=["GET","POST"])
def get_by_user_id(user_id):
    user = User.find_by_id(user_id)
    return render_template("show_user.html", user=user)
    

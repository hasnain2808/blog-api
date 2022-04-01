from flask import Blueprint
from flask_restful import Api

from blog.config import USER_BASE_URL
from blog.user.controllers import User


user_blueprint = Blueprint("user", __name__, url_prefix=USER_BASE_URL)
user_api = Api(user_blueprint)


user_api.add_resource(User, "/", "/<int:user_id>")

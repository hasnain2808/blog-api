from typing import Dict, List, Text

from flask import jsonify, request
from flask import Response
from flask_restful import Resource

from blog.constants import (
    GENERIC_ERROR_CODE,
    GENERIC_ERROR_MESSAGE,
    SUCCESS_ERROR_CODE,
    USER_DOES_NOT_EXIST_ERROR_CODE,
    INVALID_USER_ID,
    INVALID_USER_ID_ERROR_MESSAGE,
    SERIALIZER_ERROR_CODE,
    USER_DOES_NOT_EXIST_ERROR_MESSAGE,
)
from blog import app
from blog.user.dao import UserDao
from blog.user.serializers import UserSerializer


class User(Resource):
    def get(self, user_id: int) -> Response:
        try:
            user_dao_obj = UserDao()
            user: Dict = user_dao_obj.get_user(int(user_id))
            if user:
                return {
                    "status": "SUCCESS",
                    "error_code": SUCCESS_ERROR_CODE,
                    "message": user,
                }
            else:
                return jsonify(
                    {
                        "status": "ERROR",
                        "error_code": USER_DOES_NOT_EXIST_ERROR_CODE,
                        "message": USER_DOES_NOT_EXIST_ERROR_MESSAGE,
                    }
                )
        except ValueError as ve:
            return jsonify(
                {
                    "status": "ERROR",
                    "error_code": INVALID_USER_ID,
                    "message": INVALID_USER_ID_ERROR_MESSAGE,
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "status": "ERROR",
                    "error_code": GENERIC_ERROR_CODE,
                    "message": GENERIC_ERROR_MESSAGE,
                }
            )

    def post(self) -> Response:
        try:
            api_data: Dict = request.get_json()
            user_serializer = UserSerializer()
            errors: Dict = user_serializer.validate(api_data)
            if errors:
                return jsonify(
                    {
                        "status": "ERROR",
                        "error_code": SERIALIZER_ERROR_CODE,
                        "message": str(errors),
                    }
                )

            user_dao_obj = UserDao()
            error_code, message = user_dao_obj.add_user(
                api_data.get("name"), api_data.get("email")
            )

            if error_code == SUCCESS_ERROR_CODE:
                return jsonify(
                    {"status": "SUCCESS", "error_code": error_code, "message": message}
                )
            else:
                return jsonify(
                    {"status": "ERROR", "error_code": error_code, "message": message}
                )
        except Exception as e:
            return jsonify(
                {
                    "status": "ERROR",
                    "error_code": GENERIC_ERROR_CODE,
                    "message": GENERIC_ERROR_MESSAGE,
                }
            )

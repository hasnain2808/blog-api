import os
from typing import Dict, List, Set, Text, Tuple

from flask import jsonify, request
from flask_restful import Resource
from flask import Response

from blog import app
from blog.constants import (
    GENERIC_ERROR_CODE,
    GENERIC_ERROR_MESSAGE,
    SERIALIZER_ERROR_CODE,
    SUCCESS_ERROR_CODE,
    BLOG_DOES_NOT_EXIST_ERROR_CODE,
    INVALID_BLOG_ID,
    INVALID_BLOG_ID_ERROR_MESSAGE,
    BLOG_DOES_NOT_EXIST_ERROR_MESSAGE,
)
from blog.blog_post.dao import BlogPostDao
from blog.blog_post.serializers import BlogSerializer


class BlogPost(Resource):
    def post(self):
        try:
            api_data: Dict = request.get_json()
            blog_serializer = BlogSerializer()
            errors: Dict = blog_serializer.validate(api_data)
            if errors:
                return jsonify(
                    {
                        "status": "ERROR",
                        "error_code": SERIALIZER_ERROR_CODE,
                        "message": str(errors),
                    }
                )

            blog_dao_obj = BlogPostDao()
            error_code, message = blog_dao_obj.add_blog_post(
                api_data.get("user_id"), api_data.get("title"), api_data.get("content")
            )
            return jsonify({"status": error_code, "message": message})
        except Exception as e:
            return jsonify({"status": "ERROR", "message": str(e)})

    def get(self, blog_id: int) -> Response:
        try:
            blog_post_dao_obj = BlogPostDao()
            blog_post: Dict = blog_post_dao_obj.get_blog_post(int(blog_id))
            if blog_post:
                return {
                    "status": "SUCCESS",
                    "error_code": SUCCESS_ERROR_CODE,
                    "message": blog_post,
                }
            else:
                return jsonify(
                    {
                        "status": "ERROR",
                        "error_code": BLOG_DOES_NOT_EXIST_ERROR_CODE,
                        "message": BLOG_DOES_NOT_EXIST_ERROR_MESSAGE,
                    }
                )
        except ValueError as ve:
            return jsonify(
                {
                    "status": "ERROR",
                    "error_code": INVALID_BLOG_ID,
                    "message": INVALID_BLOG_ID_ERROR_MESSAGE,
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

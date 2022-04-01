from flask import Blueprint
from flask_restful import Api

from blog.config import BLOG_POST_BASE_URL
from blog.blog_post.controllers import BlogPost


blog_post_blueprint = Blueprint("blog", __name__, url_prefix=BLOG_POST_BASE_URL)
blog_post = Api(blog_post_blueprint)


blog_post.add_resource(BlogPost, "/", "/<int:blog_id>")

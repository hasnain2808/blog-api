import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "blog.db")


BLOG_POST_BASE_URL = "/blog"

USER_BASE_URL = "/user"

COMMENT_BASE_URL = "/comment"

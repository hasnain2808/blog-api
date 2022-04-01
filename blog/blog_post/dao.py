from typing import Dict, List, Set, Text, Tuple

from sqlalchemy.orm.exc import NoResultFound

from blog import db
from blog import app
from blog.blog_post.models import BlogPost
from blog.constants import GENERIC_ERROR_CODE, GENERIC_ERROR_MESSAGE, SUCCESS_ERROR_CODE
from blog.blog_post.serializers import BlogSerializer


class BlogPostDao:
    def add_blog_post(self, user_id: int, title: str, content: str) -> Tuple[int, Text]:
        try:
            blog_post = BlogPost(user_id=user_id, title=title, content=content)
            db.session.add(blog_post)
            db.session.commit()
            return (SUCCESS_ERROR_CODE, {"blog_post_id": blog_post.id})
        except Exception as e:
            return (GENERIC_ERROR_CODE, GENERIC_ERROR_MESSAGE)

    def get_blog_post(self, blog_post_id: int) -> Dict:
        blog_post = BlogPost.query.filter_by(id=blog_post_id).first()
        if blog_post:
            return BlogSerializer().dump(blog_post)
        else:
            return {}

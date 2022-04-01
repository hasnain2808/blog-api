from typing import Dict, List, Text, Tuple

from blog import db
from blog import app
from blog.user.models import User

from blog.constants import GENERIC_ERROR_CODE, GENERIC_ERROR_MESSAGE, SUCCESS_ERROR_CODE
from blog.user.serializers import UserSerializer


class UserDao:
    def get_user(self, user_id: int) -> Dict:
        user = User.query.filter_by(id=user_id).first()
        if user:
            return UserSerializer().dump(user)
        else:
            return {}

    def add_user(self, name: str, email: str) -> Tuple[int, Text]:
        try:
            user = User(name=name, email=email)
            db.session.add(user)
            db.session.commit()
            return (SUCCESS_ERROR_CODE, {"user_id": user.id})
        except Exception as e:
            print(e)
            return (GENERIC_ERROR_CODE, GENERIC_ERROR_MESSAGE)

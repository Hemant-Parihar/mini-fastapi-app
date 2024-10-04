from blog.Entities import UserEntity
from blog.model.User import UserDTO


class UserService:

    def __init__(self):
        pass

    def create_user(self, request: UserDTO, db):
        new_user = UserEntity(username=request.username, email=request.email, password=request.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_all_user(self, db):
        return db.query(UserEntity).all()

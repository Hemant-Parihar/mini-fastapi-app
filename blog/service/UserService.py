from blog.Entities import UserEntity
from blog.model.User import UserDTO
from blog.hashing import get_password_hash


class UserService:

    def __init__(self):
        pass

    @staticmethod
    def create_user(request: UserDTO, db):
        hash_password = get_password_hash(request.password)
        new_user = UserEntity(username=request.username, email=request.email, password=hash_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def get_all_user(self, db):
        return db.query(UserEntity).all()

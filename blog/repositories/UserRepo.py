from blog.Entities import UserEntity


def get_user_with_username(username: str, db):
    return db.query(UserEntity).filter(UserEntity.username == username).first()


def get_user_with_email(email: str, db):
    return db.query(UserEntity).filter(UserEntity.email == email).first()

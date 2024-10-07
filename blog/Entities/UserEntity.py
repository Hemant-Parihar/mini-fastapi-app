from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from blog.database import Base


class UserEntity(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("BlogEntity", back_populates="user")

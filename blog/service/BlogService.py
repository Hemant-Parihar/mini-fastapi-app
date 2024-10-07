from fastapi import HTTPException, status

from blog.Entities import BlogEntity


class BlogService:

    def __init__(self):
        pass

    @staticmethod
    def get_blogs(db):
        blogs = db.query(BlogEntity).all()
        return blogs

    @staticmethod
    def get_blog(id, db):
        blog = db.query(BlogEntity).filter(BlogEntity.id == id).first()
        if not blog:
            raise HTTPException(status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with {id} doesn't exists.")
        return blog

    @staticmethod
    def create_blog(request, db):
        new_blog = BlogEntity(title=request.title, body=request.body, user_id=1)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog

    @staticmethod
    def delete_blog(id, db):
        db.query(BlogEntity).filter(BlogEntity.id == id).delete(synchronize_session=False)
        db.commit()
        return "Deleted."

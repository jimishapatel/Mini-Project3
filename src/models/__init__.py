#src/models/__init__.py
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
# from .BlogPostModel import BlogPostModel, BlogpostSchema
# from .UserModel import UserModel, UserSchema


# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()
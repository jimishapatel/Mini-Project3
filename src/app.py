from flask import Flask

from .config import app_config
from .model_blog import db, bcrypt
from .view_blog.UserView import user_api as user_blueprint


def create_app(env_name):
    # app init

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    bcrypt.init_app(app)

    db.init_app(app)

    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    @app.route('/', methods=['GET'])
    def index():
        """
        test endpoint
        """
        return 'Congratulations! Your first endpoint is working'

    return app
from flask import Flask

def create_app(test_config=None):

    ''' Create and configure an instance of the Flask application. '''
    app = Flask(__name__)
    app.config.from_mapping(
    SECRET_KEY="CHANGE_THIS",
    )

    ''' Apply the blueprints to the app '''
    from .blueprints.main.views import main
    from .blueprints.blog.views import blog
    app.register_blueprint(main)
    app.register_blueprint(blog, url_prefix='/blog')
    return app
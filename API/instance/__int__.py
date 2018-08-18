from flask_api import FlaskAPI
# from flask_api import FlaskAPI
from flask import request, jsonify, abort, make_response

from validate_email import validate_email
# from flask_restful import Resource, Api

 from instance.config import app_config

 def create_app(config_name):
     
    from app.models import user,questions,answers

    app = FlaskAPI(__name__, instance_relative_config=True)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

     @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():
        pass
        
     return app

from flask import Flask
from  app.api.controllers.user_controller import user_api
from flask import Flask
from flask_injector import FlaskInjector
from app.infrastructure.dependencies import Configure

application = Flask(__name__)
application.register_blueprint(user_api)
FlaskInjector(app=application, modules=[Configure])

if __name__ == "__main__":
    application.run(host='0.0.0.0')
from flask import Flask
from my_app.config import DevConfig, ProdConfig
from my_app.tasks.controllers import taskRoute


app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)
# app.debug = True

# # decoradormain
# @app.route('/')
# def hello_world() -> str:
#     return "Hola Flask! estamos a full con RaspberryPi en modo debug"


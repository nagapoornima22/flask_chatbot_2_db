from flask import Flask,Blueprint
from app.main.controller.auth_api import index_blueprint, login_blueprint
from app.main.controller.employees_api import employees_blueprint
from app.main.controller.chatbot_api import chatbot_blueprint
from app.main.controller.chatbot_api import response_blueprint


from app.main.config.settings import TEMPLATES_FOLDER

application = Flask(__name__, template_folder=TEMPLATES_FOLDER)

application.register_blueprint(index_blueprint)
application.register_blueprint(login_blueprint)
application.register_blueprint(employees_blueprint)
application.register_blueprint(chatbot_blueprint)
application.register_blueprint(response_blueprint)

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)



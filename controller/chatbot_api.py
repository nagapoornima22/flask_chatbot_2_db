import json
import ast
from flask import Flask, Blueprint, render_template, request, jsonify
from app.main.Bot.chatbot_main import ChatBot
bot = ChatBot()

chatbot_blueprint = Blueprint('chatbot', __name__)
response_blueprint = Blueprint('response', __name__)


@chatbot_blueprint.route("/chatbot")
def home():
    return render_template("bot3.html")


@response_blueprint.route("/get", methods=['GET', 'POST'])
def get_bot_response():
    #print(request.args.get)
    userText = request.args.get('msg')
    question = request.args.get('name')
    print("usertext", userText)
    print("api :" ,question)
    res = bot.getBot().response(userText,question)
    #res = bot.getBot().response(userText)
    js_data = json.dumps(res)
    #str_data = json.loads(js_data)
    return js_data

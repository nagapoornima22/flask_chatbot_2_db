from app.main.Bot.main import ChatBot as bot

ob = bot.getBot()

i = 0
print("Print exit to leave")
while True:
    text = input("Q : ")
    if text == 'exit':
        break
    print(ob.response(text))

print("Ended successfully")
import models

class Chatbot():
    def get_response(self, message):
        if message == 'help':
            chatbot_message = 'try typing \"!! about\" or \"!! chat\" for me to respond'
        elif message == 'about':
            chatbot_message = 'Welcome to Deandra\'s chatbot where you can talk to anyone on here including me'
        elif message == 'chat':
            chatbot_message = 'I love talking to you chat anytime'
        else:
            chatbot_message = "I don't understand that command"

        new_message = models.Message(chatbot_message)
        models.db.session.add(new_message)
        models.db.session.commit()
        return chatbot_message
        
    def __init__(self):
        return

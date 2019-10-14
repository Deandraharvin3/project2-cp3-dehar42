#chatbot.py
import models, yelpAPI

class Chatbot():
    def get_response(self, message):
        message = message.lower()
        if message == 'help':
            chatbot_message = 'try typing \"!!about\", \"!!chat\", or \"!!yelp\" for me to respond'
        elif message == 'about':
            chatbot_message = 'Welcome to Deandra\'s chatbot where you can talk to anyone on here including me'
        elif message == 'chat':
            chatbot_message = 'I love talking to you chat anytime'
        elif message == 'yelp':
            chatbot_message = 'Welcome Yelp, what would you like to look for in the Baltimore area:\n for example \"!!yelp food\", \"!!yelp museum\", or \"!!yelp club\"'
        elif message[0:4] == 'yelp':
            response = yelpAPI.YelpBusinessSearch(message[4:])
            chatbot_message = response['businesses'][0]['id']
            print("Business ID: " + chatbot_message)
            
        else:
            chatbot_message = "I don't understand that command"
            
        return chatbot_message
        
    def __init__(self):
        return

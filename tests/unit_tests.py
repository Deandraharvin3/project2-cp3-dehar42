import unittest
import yelpAPI, chatbot, json

class ChatbotUnitTests(unittest.TestCase):
    
    def valid_yelp(self):
        response = (yelpAPI.YelpBusinessSearch('massage')).json()
        self.assertGreater(response['total'], 0)
    
    def invalid_yelp(self):
        response = (yelpAPI.YelpBusinessSearch('')).json()
        self.assertEquals(response['total'], 0)
        
    def bot_response_valid(self):
        bot_response = chatbot.Chatbot()
        response_help = bot_response.get_response('Help')
        print(response_help)
        self.assertEquals(response_help, 'try typing \"!!about\", \"!!chat\", or \"!!yelp\" for me to respond')
    
    def bot_response_invalid(self):
        bot_response = chatbot.Chatbot()
        response_invalid = bot_response.get_response('Hello')
        print(response_invalid)
        self.assertEquals(response_invalid, "I don't understand that command")
        
    
        
if __name__ == '__main__':
    unittest.main()
    # Make sure you make the call to run the test.
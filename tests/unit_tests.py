import unittest
import yelpAPI, chatbot, json

class ChatbotUnitTests(unittest.TestCase):
    
    def test_valid_yelp(self):
        response = (yelpAPI.YelpBusinessSearch('massage'))
        self.assertGreater(response['total'], 0)
    
    def test_invalid_yelp(self):
        response = (yelpAPI.YelpBusinessSearch('noresponse'))
        self.assertEquals(response['total'], 0)
        
    def test_bot_response_valid(self):
        bot_response = chatbot.Chatbot()
        response_help = bot_response.get_response('Help')
        response_about = bot_response.get_response('yelp museum')
        self.assertEquals(response_help, 'try typing \"!!about\", \"!!chat\", or \"!!yelp\" for me to respond')
        self.assertEquals(response_about, 'QJkcPAN-eyy8ZvWGP0NIXQ')
        
    def test_bot_response_invalid(self):
        bot_response = chatbot.Chatbot()
        response_invalid = bot_response.get_response('Hello')
        self.assertEquals(response_invalid, "I don't understand that command")
        
    def test_valid_yelp_business(self):
        response = yelpAPI.YelpBusinessId('QJkcPAN-eyy8ZvWGP0NIXQ')
        self.assertEquals(response['name'], "The Walters Art Museum")
        
    def test_invalid_yelp_business(self):
        response = yelpAPI.YelpBusinessId('nothing')
        self.assertEquals(response['error']['code'], "BUSINESS_NOT_FOUND")
        
if __name__ == '__main__':
    unittest.main()
    # Make sure you make the call to run the test.
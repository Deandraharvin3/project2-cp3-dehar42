from flask import Flask
from flask_testing import LiveServerTestCase, TestCase
import app, urllib2, unittest

class MyTest(LiveServerTestCase, TestCase):

    def create_app(self):
        test_app = app.app
        test_app.config['TESTING'] = True
        # Default port is 5000
        test_app.config['LIVESERVER_PORT'] = 8080
        # Default timeout is 5 seconds
        test_app.config['LIVESERVER_TIMEOUT'] = 10
        return test_app
        
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen(self.get_server_url())
        print(response)
        self.assertEqual(response.code, 200)
        
    def test_server_request(self):
        response = self.client.get("/")
        self.assertEquals(response, True)

if __name__ == '__main__':
    unittest.main()
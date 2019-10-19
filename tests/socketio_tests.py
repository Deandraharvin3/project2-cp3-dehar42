import app, unittest

class SocketIOTestCase(unittest.TestCase):
        
    def test_on_connect(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
        self.assertEquals(len(response), 1)
        from_server = response[0]
        self.assertEquals(
            from_server['name'], 
            "update"
        )
        data = from_server['args'][0]
        self.assertEquals(data['data'], "Got your connection!")
        client.disconnect()
        
    def test_on_disconnect(self):
        event = app.socketio.test_client(app.app)
        response = event.get_received()
        #I was expecting response to have all the socket.emit() from my app.py
        self.assertEquals(len(response), 1)
        from_server = response[0]
        #todo instead of getting disconnected, it gets update

        self.assertEquals(
            from_server['name'], 
            "disconnected"
        )
        data = from_server['args'][0]
        self.assertEquals(data['data'], "Disconnected")
        
    def test_get_message(self):
        client = app.socketio.test_client(app.app)
        response = client.get_received()
        self.assertEquals(len(response), 1)
        from_server = response[0]
        #todo instead of getting message reccieved, it gets update
        self.assertEquals(
            from_server['name'], 
            "message received"
        )
        data = from_server['args'][0]
        self.assertEquals(data['url'], False)  
    # Want to add more test case, but I can't figure it out and I ran out of time
if __name__ == '__main__':
    unittest.main()    

# project2-cp2-dehar42
## ChatBot CP 3

Created a chatbot that allows users to communicate with eachother and also use the chatbot responses to get business in baltimore from the yelp api depending on the command sent from the user. The user must login with google credintals before having access to send any messages to ensure that I have a username and profile image.

### Future Solutions
#### Finding enough unit test
I was having a hard time trying to find 10 unit test, I seperated the chatbot responses and the API calls
#### Figuing out how to work Circleci
Still cant figure out what I am doing wrong, I thought it was getting the requirements.txt just like from the lab in class
#### Adding socketio test
These test I am still confused by, I was unable to test my disconnect function, I tried creating a disconnect emit and nothing changed, I even made changes to my Main.js and Socket.js because I thought I may have needed it in those files

### Decisions
#### Unit test 
1. I can create different unit test, they tested both valid and invalid responses
2. For both the chatbot and the yelpAPI, I checked to ensure that the response worked for both valid and invalid to ensure that the user will not recieve any errors
#### Socketio test
3. Got the test for the connect function to work, couldn't get the others but I at least go that to work

#### Circleci
4. Followed everything we did in the slides, made sure that the requirements were up to date and made sure heroku was included
#### Integration test
5. This one was to test the flask web server, so I first checked if it initially worked, then I checked if the client could get the path created in the app.py

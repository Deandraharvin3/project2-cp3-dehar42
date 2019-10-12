# project2-cp2-dehar42
## ChatBot CP 2

Created a chatbot that allows users to communicate with eachother and also use the chatbot responses to get business in baltimore from the yelp api depending on the command sent from the user. The user must login with google credintals before having access to send any messages to ensure that I have a username and profile image.

### Problems
#### Adding data from the yelp api to the database: 
I keep getting a weird error that I could not figure out, I tried getting help but it still wouldn't work and I believe it may be because I am currently in python 2.7 and I didn't want to change it in the middle of completing the project
#### Adding the link to the database and keeping it as a link throught the new messages being added
#### Adding heroku configs to the react files
#### Styling
I am terrible at styling web pages I was going to do it all at the end, but that may not be a good idea
### Issues
#### Adding the links: 
I was trying to figure out which library worked best with heroku and was avalible in python 2.7. So I used the rfc3987 library to parse the url to determine if the message was a url or not
#### Adding requests from API call: 
I forgot to import request and install request, after doing that I realized that I had an error in heroku and I forgot to add request to my requerments.txt file
#### Having to query the Yelp API:
We did this in project 1, but I wanted to find the best way to get the data, since I was having a problem trying to get multiple businesses to show to the screen, I decided to just query the top business and try to add that to my database
#### Disabling Send button when user is not logged in:
I had a hard time with this because I was trying to do disable the button in my Content.js file when I should have been doing this in my Button.js file. After figuring out how to check and see if the user is logged in, it was easy to disable and enable the button.

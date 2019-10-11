    
import * as React from 'react';
import { Button } from './Button';
import { Socket } from './Socket';

export class Content extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'message': [],
            login: ''
        };
    }
    
    chatbotResponse() {
        if (this.state.bot_response != '') {
            if (this.state.yelp_response != '') {
                console.log("Recieved yelp data");
                return <a href={this.state.yelp_response}> {this.state.bot_response} </a>;
            } else {
                return <text> {this.state.bot_response} </text>;
            }
        }
    }
    
    componentDidMount() {
        Socket.on('update', (data) => {
            this.setState({
                'old_messages': data['previous_messages']
            });
        });
        Socket.on('google keys', (data) => {
            this.setState({
                'Google_id': data['GoogleID'],
                'secret': data['GoogleSecret']
            });
        });
        Socket.on('message received', (data) => {
            console.log("Content recieved length: ");
            this.setState({
                'old_messages':data['chat'],
                'number_received': data['message'],
                'url': data['url'],
                'username': data['username'],
                'profileImage': data['profilePic'],
                'bot_response': data['bot_response'],
                'yelp_response': data['yelp_url'],
                'number_connected': data['connected']
            });
            console.log('URL: ', this.state.url);
            console.log('USERNAME: ', this.state.username);
        });
    }
        
    render() {
        const isUrl = this.state.url;
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
        <h1>Welcome to Chatbot</h1>
        <h3> Number of users: {this.state.number_connected} </h3> 
        <ul>
        <li>{this.state.old_messages}</li>
        <img src={this.state.profileImage} /> <b>{this.state.username}</b> <br />
        { isUrl ? (
            <a href={this.state.number_received}> {this.state.number_received} </a>
            ) : (
            <text> {this.state.number_received} </text>
            )}
        <chatbotResponse />
            
            <Button />
        </ul>
        </div>;

    }
}
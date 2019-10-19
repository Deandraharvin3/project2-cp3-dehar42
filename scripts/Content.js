    
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
    
    componentDidMount() {
        Socket.on('update', (data) => {
            this.setState({
                'old_messages': data['previous_messages']
            });
        });
        
        Socket.on('disconnected', (data) => {
            this.setState({
                'disconnected': data['data']
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
        });
    }
    render() {
        const isUrl = this.state.url;
        let isYelp = false;
        const chatbot = this.state.bot_response;
        const yelp = this.state.yelp_response;
        if(yelp != ''){
            console.log("Recieved yelp response: ", this.state.yelp_response);
            isYelp = true;
        }
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
        { isYelp ? (
            <a href={this.state.yelp_response}> {chatbot} </a>
        ) : (
            <text> {chatbot} </text>
        )}
            
            <Button />
        </ul>
        </div>;

    }
}
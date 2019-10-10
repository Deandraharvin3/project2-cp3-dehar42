    
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
                'bot_response': data['bot_response']
            });
            console.log('URL: ', this.state.url);
            console.log('USERNAME: ', this.state.username);
        });
    }
        
    render() {
        const isUrl = this.state.url;
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
        <h1>Hello</h1>
        <ul>
        <li>{this.state.old_messages}</li>
        <b>{this.state.username}</b> <br />
        { isUrl ? (
            <a href={this.state.number_received}> {this.state.number_received} </a>
            ) : (
            <text> {this.state.number_received} </text>
            )}
            
            <b>Chatbot</b> <br />
            <text> {this.state.bot_response} </text>
            <Button />
        </ul>
        </div>;

    }
}
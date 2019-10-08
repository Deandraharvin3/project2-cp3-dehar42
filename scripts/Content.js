    
import * as React from 'react';
import { Button } from './Button';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

const responseGoogle = (response) => {
  console.log(response);
  this.setState({login: response});
  Socket.emit('user signin', {'user': response.text});
  console.log("Sent data to Button.js and app.py");
}; 
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
                'id': data['GoogleID'],
                'secret': data['GoogleSecret']
            })
        })
        Socket.on('message received', (data) => {
            console.log("Content recieved length: ");
            this.setState({
                'old_messages':data['chat'],
                'number_received': data['message'],
                'url': data['url']
            });
            console.log('URL: ', this.state.url);
        });
    }
        
    render() {
        const enabled = this.state.login != '';
        const isUrl = this.state.url;
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
        <h1>Hello</h1>
        <ul>
        <li>{this.state.old_messages}</li>
        { isUrl ? (
            <a href={this.state.number_received}> {this.state.number_received} </a>
            ) : (
            <text> {this.state.number_received} </text>
            )}
            <Button disabled={!enabled}/>
        </ul>
        <div>
            <GoogleLogin
                  clientId={this.state.id}
                  buttonText="Login"
                  onSuccess={responseGoogle}
                  onFailure={responseGoogle}
                  cookiePolicy={'single_host_origin'}
                />        
        </div>
        </div>;

    }
}
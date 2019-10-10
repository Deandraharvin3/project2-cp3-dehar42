import * as React from 'react';

import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';

export class Button extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      enabled: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }
    
  handleChange(event) {
      this.setState({value: event.target.value});
  }
  
  handleSubmit(event) {
    event.preventDefault();
    
     // this is a local variable so we don't need to initialize in the constructor
    console.log('Sending message: ', this.state.value);
    Socket.emit('new message', 
    {
      'message': this.state.value,
      'username': this.state.signin
    });
    console.log('Sent a message to server from ', this.state.signin);
  }
  
  render() { 
    const responseGoogle = (response) => {
      this.setState({'signin': response, enabled: true});
      console.log(response);
    };
    return (
      <form onSubmit={this.handleSubmit}>
         <GoogleLogin
                  clientId='307723243221-48famr48tnm99bv85v7odvrthhakarur.apps.googleusercontent.com'
                  buttonText="Login"
                  onSuccess={responseGoogle}
                  onFailure={responseGoogle}
                  cookiePolicy={'single_host_origin'}
            />   
        <label>
          Message:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" disabled={!this.state.enabled}/>
      </form>
    );
  }
}
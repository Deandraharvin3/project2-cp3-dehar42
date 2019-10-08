import * as React from 'react';

import { Socket } from './Socket';

export class Button extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
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
    Socket.emit('new message', {'message': this.state.value});
    console.log('Sent a message to server!');
  }
  
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Message:
          <input type="text" value={this.state.value} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }
}
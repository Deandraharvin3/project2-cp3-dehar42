    
import * as React from 'react';
import TextInput from 'react-textinput-field';
import { Button } from './Button';
import { Socket } from './Socket';
import {MyFavoriteFoodHeader} from './MyFavoriteFoodHeader.js';
import {MyFavoriteFoodList} from './MyFavoriteFoodList.js';

const query = {
  text: 'SELECT * FROM message',
  types: {
    getTypeParser: () => val => val,
  },
};

export class Content extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'numbers': []
        };
    }
    componentDidMount() {
        Socket.on('message received', (data) => {
            console.log("Content recieved message");
            this.setState({
                'number_received': data['message']
            });
        });
    }
    render() {
        let my_rand_num = this.state.number_received;
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '500px', border: '1px solid #000'}}>
        <h1>Hello</h1>
        <ul>{my_rand_num}</ul> 
        <Button />
        </div>;
    }
}
    
import * as React from 'react';
import TextInput from 'react-textinput-field';
import { Button } from './Button';
import { Socket } from './Socket';
import {MyFavoriteFoodHeader} from './MyFavoriteFoodHeader.js';
import {MyFavoriteFoodList} from './MyFavoriteFoodList.js';

let isUrl = '';

export class Content extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            'message': []
        };
    }
    
    componentDidMount() {
        Socket.on('message received', (data) => {
            console.log("Content recieved");
            this.setState({
                'number_received': data['message'],
                'url': data['url']
            });
            console.log('URL: ', this.state.url);
            if (this.state.url == 'True') {
                console.log("Received a URL");
                isUrl = true;
            } else {
                isUrl = false;
            }
        });
        console.log("Testing");
    }

    render() {
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '1000px', border: '1px solid #000'}}>
        <h1>Hello</h1>
        <body>
        { isUrl ? (
            <a href={this.state.message} />
            ) : (
            <text> {this.state.number_received} </text>
            )}
            <Button />
        </body>
        </div>;
    }
}
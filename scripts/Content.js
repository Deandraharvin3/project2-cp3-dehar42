    
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
            'numbers': [5, 7, 10, 30]
        };
    }
    
    componentDidMount() {
        Socket.on('number received', (data) => {
            this.setState({
                'number_received': data['number']
            });
        });
    }
  
    render() {
        let my_rand_num = this.state.number_received;
        var my_food = ['food'];
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '500px', border: '1px solid #000'}}>
        <MyFavoriteFoodHeader />
        <MyFavoriteFoodList food={my_food} />
        <ul>{query}</ul>
        <Button />
        </div>;
    }
}
import * as React from 'react';
import * as ReactDOM from 'react-dom';

import { Content } from './Content';
import { Socket } from './Socket';
import { Socket_dis } from './Socket';

ReactDOM.render(<Content />, document.getElementById('content'));

Socket.on('connect', function() {
    console.log('Connecting to the server!');
});

Socket_dis.on('disconnected', function() {
    console.log('Somone disconnected');
})
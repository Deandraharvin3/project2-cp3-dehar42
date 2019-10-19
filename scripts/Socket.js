import * as SocketIO from 'socket.io-client';

export var Socket = SocketIO.connect();
export var Socket_dis = SocketIO.disconnect();
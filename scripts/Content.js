    
import * as React from 'react';

var http = require("https");

var options = {
	"method": "GET",
	"hostname": "api.chatbot.com",
	"port": null,
	"path": "/stories",
	"headers": {
		"authorization": "Bearer ${MiYLzDMtDWPZB2cBdatNme6Jdbr86N0_}"
	}
};

var req = http.request(options, function (res) {
	var chunks = [];

	res.on("data", function (chunk) {
		chunks.push(chunk);
	});

	res.on("end", function () {
		var body = Buffer.concat(chunks);
		console.log(body.toString());
	});
});

req.end();

export class Content extends React.Component {
    render() {
        return <div><h1>Welcome to the Chat Bot!</h1>
        <body></body>
        <input />
        <button>Send</button></div>;
    }
}
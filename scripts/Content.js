    
import * as React from 'react';
import {MyFavoriteFoodHeader} from './MyFavoriteFoodHeader.js';
import {MyFavoriteFoodList} from './MyFavoriteFoodList.js';

var bottomText = {
	positon: 'absolute',
	bottome: 0
};
var know = {
    "hello" : "hi",
    "how are you?" : "good",
    "ok" : ":)"
    };
    
function talk() {
    var user = document.getElementById("userBox").value;
    document.getElementById("userBox").value = "";
    document.getElementById("chatLog").innerHTML += user+"<br>";
    if (user in know) {
        document.getElementById("chatLog").innerHTML += know[user]+"<br>";
        } else {
            document.getElementById("chatLog").innerHTML += "I don't understand...<br>";
            }
} 
export class Content extends React.Component {
    render() {
    	let my_food = ['sushi', 'meat', 'eggs', 'yams'];
        return <div style={{backgroundColor: 'white', position: 'absolute', left: '25%', width: '700px', height: '500px', border: '1px solid #000'}}>
        <MyFavoriteFoodHeader />
        <MyFavoriteFoodList food={my_food} />
        <input type="text" id= "userMessage" name="Enter message" position={bottomText} bottom="0"/>
    
        <output form="message" name="x" for="userMessage"></output>

        </div>;
    }
}
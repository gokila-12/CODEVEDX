const chatArea=document.getElementById("chat-area");

const input=document.getElementById("message");

input.addEventListener("keypress",function(e){

if(e.key==="Enter")
sendMessage();

});

function addUser(message){

chatArea.innerHTML+=`

<div class="user">

<div class="message">

${message}

</div>

<div class="avatar">

👤

</div>

</div>

`;

chatArea.scrollTop=chatArea.scrollHeight;

}

function addBot(message){

chatArea.innerHTML+=`

<div class="bot">

<div class="avatar">

🤖

</div>

<div class="message">

${message}

</div>

</div>

`;

chatArea.scrollTop=chatArea.scrollHeight;

}

async function sendMessage(){

const message=input.value.trim();

if(message==="")
return;

addUser(message);

input.value="";

const response=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:message

})

});

const data=await response.json();

addBot(data.reply);

}

async function quickQuestion(question){

addUser(question);

const response=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:question

})

});

const data=await response.json();

addBot(data.reply);

}

function newChat(){

chatArea.innerHTML=`

<div class="bot">

<div class="avatar">

🤖

</div>

<div class="message">

Hello 👋<br><br>

Welcome to Internal Helpdesk.<br>

How can I help you today?

</div>

</div>

`;

}
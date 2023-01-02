var username=JSON.parse(document.getElementById('username').textContent)

var roomid=JSON.parse(document.getElementById('roomid').textContent)

const objdiv=document.querySelector('.chat-message')
objdiv.scrollTop=objdiv.scrollHeight;



if (roomid!=""){
    const newweb=new WebSocket(
        'ws://'
        +window.location.host
        +'/ws/room/'+
        roomid+
        '/'
        
    );
    

    newweb.onmessage=function(e){
        const mesdata=JSON.parse(e.data)
        var date=new Date().toLocaleTimeString();
        if(mesdata.message !="None"){
            var html=`<ul><li><span><b>${mesdata.username}</b></span>
                <p>${mesdata.message}<p>
                <time>${date}</time></li></ul>`
            
            document.querySelector('#chat-message').insertAdjacentHTML("beforebegin",html);
            const objdiv=document.querySelector('.chat-message')
            objdiv.scrollTop=objdiv.scrollHeight;
        }
        


    }
    
    document.querySelector('#chat-message-submit').onclick=function(e){
        const messagetag=document.getElementById("sendmessage");
        const message=messagetag.value;
        newweb.send(JSON.stringify({
            "message":message,
            "room":roomid,
            "username":username
        }))
        const objdiv=document.querySelector('.chat-message')
        objdiv.scrollTop=objdiv.scrollHeight;
        
    }




    
    const objdiv=document.querySelector('.chat-message')
    objdiv.scrollTop=objdiv.scrollHeight;
    
}


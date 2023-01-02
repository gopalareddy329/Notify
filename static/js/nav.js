var username=JSON.parse(document.getElementById('username').textContent)


const openl=document.querySelector("#open");
const closel=document.querySelector("#close");
const mainl=document.querySelector("#mainmenu");

const openmenu=document.querySelector("#openmenu");
const joinbutton=document.querySelector('#join')
const createbutton=document.querySelector('#createroom')
createbutton.addEventListener('click',createroom)
function createroom(){
    createform=document.querySelector("#createform")
    createform.style.display="block"
    const createinput=document.querySelector("#createid")
    joininput.onsubmit(function(){createform.style.display="none"})
   
}

joinbutton.addEventListener('click',join)
function join(){
    joinform=document.querySelector("#joinform")
    joinform.style.display="block"
    const joininput=document.querySelector("#joinid")
    joininput.onsubmit(function(){joinform.style.display="none"})
   
}


let count=0;
openmenu.addEventListener('click',openlist)
const changemenu=document.querySelector('#menu-container')
function openlist(){
    if(count%2 == 0){
        changemenu.style.display="block";
        
    }
    else{
        changemenu.style.display="none";
    }
    count+=1;
    
}



openl.addEventListener('click',show);
closel.addEventListener('click',stop);
function show(){
    mainl.style.display='flex';
    mainl.style.marginTop='0';
    
    openl.style.display='none';
}
function stop(){
    mainl.style.marginTop='-1000px'
    openl.style.display='block';
}
var roomname="universal"


const web=new WebSocket(
    'ws://'
    +window.location.host
    +'/ws/'+
    roomname+
    '/'
    
);
web.onmessage=function(e){
    
    const data=JSON.parse(e.data);
    if (data.message){
        var obj=data.message
        obj=JSON.parse(obj)
        var payload=`<li>${obj.notification}</li>`
        document.querySelector('.content').insertAdjacentHTML("afterbegin",payload);

    }else{
        alert("The message use empty")
    }
}


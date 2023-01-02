




document.querySelector("#room-copy-id").onclick=function (){
    var roomid = document.getElementById("copy-id");
    const hover=document.querySelector("#hover-room-name")
    hover.style.display="block";
    hover.innerHTML=roomid.value
}
var usercount=0
    const userlist=document.querySelector("#users-list-box")
    document.querySelector("#user-list-open").onclick=function(){
        if(usercount%2 == 0){
            userlist.style.display="block";
            
        }
        else{
            userlist.style.display="none";
        }
        usercount+=1;
    }

    
    var password=""
    var password2
    let passwords=document.querySelectorAll(".cpassword")
    for(var i=0;i<passwords.length;i++){
        passwords[i].onkeyup=function(){
            password=passwords[0].value
            password2=passwords[1].value
            if(password!=password2 || password.length<8 ){

                document.querySelector("#signup-submit").disabled=true

                }
                else{
                document.querySelector("#signup-submit").disabled=false
                }
        }
    }
    
    

    

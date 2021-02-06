// document.getElementById("edit_profile").addEventListener("click",editProfile())
let editable=document.getElementsByClassName("editable")
function editProfile(){
    console.log("you requested to edit profile");
    document.getElementById("username").contentEditable="true";
    document.getElementById("userbio").contentEditable="true";
    document.getElementById("usercollege").contentEditable="true";
    document.getElementById("profile_photo_input").style.display="inline-block";
    
}
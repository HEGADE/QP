filter_open=document.getElementById("filter-btn")
filter_items=document.getElementById("filter_items")

close_filterItems=document.getElementById("close_filterItems")
// select_university=document.getElementById("university")

// select_first=document.getElementById("college")

let menu= document.getElementById("menu");
let user= document.getElementById("user");
function open_filter(){
    console.log("clicked filter button");
    filter_items.style.display="flex";
}
function close_filter(){
    console.log("clicked close filter button");
    filter_items.style.display="none";
}

document.getElementById("user").addEventListener("click",()=>{
    menu.style.display="flex";
    user.classList.add("user_absolute")
    
    
})
document.getElementById("close_menu").addEventListener("click",()=>{
    user.classList.remove("user_absolute")
    menu.style.display="none";
})


// function sel_First_Func() {
//     console.log('You have changed the filter');
//     console.log("value "+select_first.value);
//     const value=select_first.value;

//     // Instantiate an xhr object
//     const xhr = new XMLHttpRequest();
//     url =`http://127.0.0.1:8000/json_${value}`;
//     console.log(url);
//     // Open the object
//     xhr.open('GET',url, true);


//     // What to do when response is ready
//     xhr.onload = function () {
//         if(this.status === 200){
//             let obj = JSON.parse(this.responseText);
//             console.log(obj);
//             let str;
//             for (key in obj)
//             {
//                 str =obj[key].fields.university;
//                 console.log(str);
//                 let option =document.createElement("option")
//                 option.text=str
//             option.name="university";
//             option.value=str;
//             select_university.appendChild(option);
//                 str = "";
//             }
//         }
//         else{
//             console.log("Some error occured")
//         }
//     }

//     // send the request
//     xhr.send();
//     console.log("We are done fetching filter item!");
    
// }




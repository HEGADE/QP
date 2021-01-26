let selector_university = document.getElementById("university");
let selector_course = document.getElementById("course");
let selector_year = document.getElementById("year");
let selector_subject = document.getElementById("subject");

let select_first=document.getElementById("college");
let select_second=document.getElementById("university");
let select_third=document.getElementById("course");
let select_four=document.getElementById("year");
let select_college=document.getElementById("college");

let university;
let college;
let course;
let paperr;
let subject;
let year;
let examination;

let options=`<option>--select--</option>`


function get_filter_first_option() {
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/filter_first_option`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;
        console.log(`university: ${university}`);
        console.log(`course: ${course}`);
        console.log(`college: ${college}`);
        console.log(`paper: ${paper}`);
        console.log(`provider: ${provider}`);
        console.log(`subject: ${subject}`);
        console.log(`year: ${year}`);
        console.log(`examination: ${examination}`);

        let option = ` <option value="${college}" name="${college}">${college}</option>`
        options+=Option
        
      }
      select_college.innerHTML=options
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
  console.log("We are done fetching filter item!");
}

function sel_First_Func() {
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value = select_first.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value}`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;
        console.log(`university: ${university}`);
        console.log(`course: ${course}`);
        console.log(`college: ${college}`);
        console.log(`paper: ${paper}`);
        console.log(`provider: ${provider}`);
        console.log(`subject: ${subject}`);
        console.log(`year: ${year}`);
        console.log(`examination: ${examination}`);

        let option = document.createElement("option");
        option.text = university;
        option.setAttribute("name","university");
                option.value = university;
        selector_university.appendChild(option);
        university = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
  console.log("We are done fetching filter item!");
}

function sel_Sec_Func() {
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value1 = select_first.value;
  const value2 = select_second.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value1}/${value2}`.replace(" ","");
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;
        console.log(`university: ${university}`);
        console.log(`course: ${course}`);
        console.log(`college: ${college}`);
        console.log(`paper: ${paper}`);
        console.log(`provider: ${provider}`);
        console.log(`subject: ${subject}`);
        console.log(`year: ${year}`);
        console.log(`examination: ${examination}`);

        let option = document.createElement("option");
        option.text = course;
        option.setAttribute("name","course"); 
        option.value = course;
        selector_course.appendChild(option);
        course = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
  console.log("We are done fetching filter item!");
}

function sel_Third_Func() {
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value1}/${value2}/${value3}`;
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;
        console.log(`university: ${university}`);
        console.log(`course: ${course}`);
        console.log(`college: ${college}`);
        console.log(`paper: ${paper}`);
        console.log(`provider: ${provider}`);
        console.log(`subject: ${subject}`);
        console.log(`year: ${year}`);
        console.log(`examination: ${examination}`);

        let option = document.createElement("option");
        option.text = year;
        option.setAttribute("name","year");
        option.value=year
        selector_year.appendChild(option);
        year = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
  console.log("We are done fetching filter item!");
}

function sel_Four_Func() {
  console.log("You have changed the filter");
  console.log("value " + select_first.value);
  const value1 = select_first.value;
  const value2 = select_second.value;
  const value3 = select_third.value;
  const value4 = select_four.value;

  // Instantiate an xhr object
  const xhr = new XMLHttpRequest();
  url = `http://127.0.0.1:8000/json-${value1}/${value2}/${value3}/${value4}`.replace(" ","");
  console.log(url);
  // Open the object
  xhr.open("GET", url, true);

  // What to do when response is ready
  xhr.onload = function () {
    if (this.status === 200) {
      let obj = JSON.parse(this.responseText);
      console.log(obj);
      let str;
      for (key in obj) {
        university = obj[key].fields.university;
        examination = obj[key].fields.examination;
        college = obj[key].fields.college;
        course = obj[key].fields.course;
        paper = obj[key].fields.paper;
        provider = obj[key].fields.provider;
        subject = obj[key].fields.subject;
        year = obj[key].fields.year;
        console.log(`university: ${university}`);
        console.log(`course: ${course}`);
        console.log(`college: ${college}`);
        console.log(`paper: ${paper}`);
        console.log(`provider: ${provider}`);
        console.log(`subject: ${subject}`);
        console.log(`year: ${year}`);
        console.log(`examination: ${examination}`);

        let option = document.createElement("option");
        option.text = subject;
        option.setAttribute("name","subject")
        option.value = subject;
        selector_subject.appendChild(option);
        subject = "";
      }
    } else {
      console.log("Some error occured");
    }
  };

  // send the request
  xhr.send();
  console.log("We are done fetching filter item!");
}
// function setfilter() {
//   let AfterFilter = `<div class="colleges">

//         <div class="titles">
//             <h1>${college}<img src="{%static 'question_papers/images/college.png' %}" alt="#">
//             </h1>
//             <h1>${university}{% if ${university} == 'Mangolre University' %}
//                 <img src="{%static 'question_papers/images/mangloreuniversity.jpg'%}" alt="#">
//                 {% elif ${university}== 'Kuvempu University'%}
//                 <img src="{%static 'question_papers/images/Kuvempu_University.jpg'%}" alt="#">
//                 {% else %}
//                 <img src="{%static 'question_papers/images/university.jpg'%}" alt="#">
//                 {% endif %} </h1>
//             <h1>${course} <img src="{%static 'question_papers/images/course.png'%}" alt="#">
//             </h1>
//             <a href="../">
//                 <h1>${year} <img src="{%static 'question_papers/images/year.png'%}" alt="#">
//                 </h1>
//             </a>
//             <h1>${subject}<img src="{%static 'question_papers/images/subject.jpg'%}" alt="#"></h1>
//         </div>
//         <div class="paper">
           
//             <div class="paper">
//                 <div id="row">
//                     <a href="{{${paper}.url}}" target="_blank">
//                         <h1 id="paper">${examination} : </h1>
//                     </a>
//                     <div class="icons">
//                         <!-- <td><a href="{{${paper}.url}}" target="_blank">Open</a></td> -->
//                         <a href="{{${paper}.url}}" download class="fa fa-download link"" aria-hidden=" true">
//                             <p></p>
//                         </a>
//                         <i class="fa fa-share link" aria-hidden="true" id="share">
//                             <p></p>
//                         </i>
//                     </div>
//                 </div>
//                 </div>
                
//             `;

//   result.innerHTML = AfterFilter;
// }


// function getUser() {  
//     fetch('http://localhost:5000/users')
//         .then(res =>  res.json())
//         .then(data => {
//             let users = document.getElementById('users');
//             for( let i = 0; i < data.length; i++){
//                 let row = document.createElement('tr');

//                 let name = document.createElement('td');
//                 name.innerHTML = data[i].user_name;
//                 row.appendChild(name);
                
//                 let email = document.createElement('td');
//                 email.innerHTML = data[i].email;
//                 row.appendChild(email);
//                 users.appendChild(row);
//             }
//         })
//     }
// getUser();


// This works to save a new user to the db without refreshing the page and showing up imidiately in the table and clearing the form
    let myForm = document.getElementById('myForm');
    myForm.onsubmit = function(e){
        // "e" is the js event happening when we submit the form.
        // e.preventDefault() is a method that stops the default nature of javascript.
        e.preventDefault();
        // create FormData object from javascript and send it through a fetch post request.
        let form = new FormData(myForm);
        // this how we set up a post request and send the form data.
        fetch("http://localhost:5000/create/user", { method :'POST', body : form})
            .then( response => response.json() )
            // .then( data => console.log("this is data" + data) )
            .then( data => {
                if (data.error){
                    console.log(data.error)
                    document.getElementById('error_message').textContent = data.error
                }
                else{
                    console.log("this is data message: " + data.message)
                    let users = document.getElementById('users');

                    let row = document.createElement('tr')

                    new_name=document.createElement('td');
                    new_name.innerHTML=data.user_name;
                    console.log(data.user_name)
                    row.append(new_name)
                                    
                    let email = document.createElement('td');
                    email.innerHTML = data.email;
                    console.log(data.email)
                    row.append(email);
                    users.append(row);
                    document.getElementById("myForm").reset();
                }
            });
    }


// $(document).ready(function() {
//     $('.myForm').submit(function (e) { 
//         e.preventDefault();

//         var response = $.post('http://localhost:5000/create/user', $('.myForm').serialize());
//         console.log("RESPONSE" + response);
//         response.done(function (data) { 
//             console.log(data)
//             $('.users').append(data)
//         })
//     })

// })


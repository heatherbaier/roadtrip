function add_trip() { 

    var form = document.createElement("form");
    form.setAttribute("method", "post");

    // Create an input element for Full Name
    var trip_name = document.createElement("input");
    trip_name.setAttribute("type", "text");
    trip_name.setAttribute("id", "trip-name");
    trip_name.setAttribute("name", "Trip Name");
    trip_name.setAttribute("placeholder", "Summer 2021 Roadtrip");

    // create a submit button
    var submit = document.createElement("button");
    submit.innerHTML = "Add Trip"; 
    submit.onclick = function () {

        var trip_name = document.getElementById('trip-name').value;

        fetch('/add-trip', {

            // When the data gets POSTed back to Flask, it'll be in JSON format
            headers: {
                "Access-Control-Allow-Headers" : "*",
                "Access-Control-Allow-Origin" : "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
                'Content-Type': 'application/json'
            },            
            method: 'POST',
            body: JSON.stringify({
                "trip_name": trip_name
            })

        }).then(function (response) {
            return response.text();
        }).then(function (text) {
            var new_trip_card = document.createElement("div");
            new_trip_card.innerHTML = "Create new trip"; 
            var icon = document.createElement("i");
            icon.innerHTML = "travel_explore"; 
            new_trip_card.appendChild(icon);
            document.getElementById("trips").appendChild(new_trip_card);
        })

    }

    // Append the full name input to the form
    form.appendChild(trip_name);
    form.appendChild(submit);
    document.getElementById("create-trip").appendChild(form);
        
}


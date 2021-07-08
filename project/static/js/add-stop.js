function add_stop(trip_name) { 

    console.log(trip_name);

    var form = document.createElement("form");
    form.setAttribute("method", "post");

    // Create an input element for Full Name
    var stop_name = document.createElement("input");
    stop_name.setAttribute("type", "text");
    stop_name.setAttribute("id", "stop-name");
    stop_name.setAttribute("name", "Stop Name");
    stop_name.setAttribute("placeholder", "Williamsburg, VA");

    // create a submit button
    var submit = document.createElement("button");
    submit.setAttribute("id", "submit-trip");
    submit.innerHTML = "Add stop"; 

    submit.onclick = function () {

        var stop_name = document.getElementById('stop-name').value;

        console.log(stop_name);

        // var geocoder;

        // geocoder = new google.maps.Geocoder();

        // console.log('here!')

        // geocoder.geocode( { 'address': stop_name}, function(results, status) {
        //     if (status == 'OK') {
        //       console.log(results[0].geometry.location);
        //       var coords = results[0].geometry.location;
        //     } else {
        //         alert('Geocode was not successful for the following reason: ' + status);
        //     }
        // })
      


        axios.post('http://127.0.0.1:5000/add-stop', {
            "stop_name": stop_name,
            "trip_name": trip_name
          })
          .then(function (response) {
            console.log(response);
          })

        console.log('back here!');


        var new_stop_card = document.createElement("div");
        new_stop_card.innerHTML = stop_name; 
        var delete_stop_button = document.createElement("button");
        delete_stop_button.innerHTML = "Delete Stop";

        new_stop_card.appendChild(delete_stop_button);
        var stop_section = document.getElementById("stops");
        stop_section.appendChild(new_stop_card);

    }

    // Append the full name input to the form
    form.appendChild(stop_name);
    form.appendChild(submit);
    document.getElementById("add-stop").appendChild(form);

    var input = document.getElementById('stop-name');
    new google.maps.places.Autocomplete(input);  

    document.getElementById("submit-trip").addEventListener("click", function() {
        // document.getElementById("demo").innerHTML = "Hello World";

        var new_stop_card = document.createElement("div");
        new_stop_card.innerHTML = stop_name; 
        var delete_stop_button = document.createElement("button");
        delete_stop_button.innerHTML = "Delete Stop";

        new_stop_card.appendChild(delete_stop_button);
        var stop_section = document.getElementById("stops");
        stop_section.appendChild(new_stop_card);

      });    

}


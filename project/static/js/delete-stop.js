function delete_stop(stop_name, trip_name) { 

    console.log(stop_name);

    fetch('http://127.0.0.1:5000/delete-stop', {

        // When the data gets POSTed back to Flask, it'll be in JSON format
        headers: {
            "Access-Control-Allow-Headers" : "*",
            "Access-Control-Allow-Origin" : "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            'Content-Type': 'application/json'
        },            
        method: 'POST',
        body: JSON.stringify({
            "stop_name": stop_name,
            "trip_name": trip_name
        })

    }).then(function (response) {
        return response.text();
    }).then(function (text) {

        var to_delete = document.getElementsByClassName(stop_name);
        var stops_div = document.getElementById("stops");

        for (i = 0; i < to_delete.length; i++) {
            to_delete[i].remove();
            stops_div.style.columnCount -= 1
        }

    })

}

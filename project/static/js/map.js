

var mymap = L.map('map').setView([23.6345, -102.5528], zoom_start = 7);
L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
    maxZoom: 20,
    attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
}).addTo(mymap);


axios.get("http://127.0.0.1:5000/map-stops/{{ trip_name }}")

    .then(response => {

        var stations = L.geoJSON(response.data, {onEachFeature: onEachFeature})//.addTo(mymap);
        window.stations = stations;
        window.stations.addTo(mymap);

    }) 


// On each feature, highlight/remove highlight when hovered over, zoom when clicked and add popup
function onEachFeature(feature, layer) {
    layer.bindPopup(feature.properties.stopID);
}
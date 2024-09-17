function our_layers (map, options) {
        var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        });

        
        var OpenTopoMap = L. tileLayer("http://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", { 
            maxZoom: 17,
            attribution: 'Map data: &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/CC-BY-SA</a>)'

        });
        
        var points = new L.GeoJSON.AJAX ("/map/lieuxInteret",{
            onEachFeature: function(feature, layer){
                layer.bindPopup(feature.properties.name.toString());
            }
        });

        var departements = new L.GeoJSON.AJAX ("/map/limiteDepFr",{
            style: function colors(feature){ 
                    var baseStyle = {
                        weight: 1 // Apply thin borders to all dep
                    };

                    switch(feature.properties.nom){
                        case 'Herault':
                            baseStyle.color = 'red';
                            baseStyle.fillOpacity = 0.06;
                            break;
                    }

                    return baseStyle;
                },
            onEachFeature: function(feature, layer){
                layer.bindPopup(feature.properties.nom.toString());
            }
        });
        points.addTo(map);
        departements.addTo(map);

        var baseLayers = {
            "OSM":osm,
            "OpenTopoMap" : OpenTopoMap
        }
        
        var groupedOverlays = {
            "Layers": {
                "Departements": departements
            },
            "Points of Interest": {
                "Saved Places": points
            }
        };

        L.control.groupedLayers(baseLayers, groupedOverlays).addTo(map);

        L.Routing.control({
            waypoints: [
                L.latLng(43.611316,3.883045),
                L.latLng(43.609282, 3.917234)
            ]
        }).addTo(map);
}
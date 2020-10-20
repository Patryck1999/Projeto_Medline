endereco = document.querySelector("span[name=endereco]").innerHTML
        mapboxgl.accessToken = 'pk.eyJ1IjoiZGlqYWlyIiwiYSI6ImNrZ2Z4ZjNzdDBweHoycXBpaDBvYmJ4Y3AifQ.FJQ2CvE4EhcCWxqrFP-4Lw';
        var mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });
        mapboxClient.geocoding
            .forwardGeocode({
                query: endereco,
                autocomplete: false,
                limit: 1
            })
            .send()
            .then(function (response) {
                if (
                    response &&
                    response.body &&
                    response.body.features &&
                    response.body.features.length
                ) {
                    var feature = response.body.features[0];

                    var map = new mapboxgl.Map({
                        container: 'map',
                        style: 'mapbox://styles/mapbox/streets-v11',
                        center: feature.center,
                        zoom: 16
                    });

                    var popup = new mapboxgl.Popup({ offset: 25 }).setText(
                    endereco
                    );

                    new mapboxgl.Marker().setLngLat(feature.center).setPopup(popup).addTo(map);
                }
            });
            
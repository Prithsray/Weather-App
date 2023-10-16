document.addEventListener('DOMContentLoaded', () => {
    const options = {
        // Required: API key
        key: 'nYoAcnaiJ7GOkcIS39DWZvUivfWJdEBX', // REPLACE WITH YOUR KEY !!!

        // Put additional console output
        verbose: true,
    };

    const { windyInit } = window;
    let latitude, longitude;

    // Function to initialize the Windy map
    function initWindyMap() {
        windyInit(options, windyAPI => {
            const { map } = windyAPI;

            // Add a popup with a default location (e.g., Prague)
            L.popup()
                .setLatLng([50.4, 14.3])
                .setContent('Hi')
                .openOn(map);

            // Event listener for the "Get Coordinates" button
            document.getElementById('getCoordinates').addEventListener('click', () => {
                const city = document.getElementById('cityInput').value;

                // Use a geocoding service to get coordinates based on the city name
                const geocodingUrl = `https://nominatim.openstreetmap.org/search?format=json&q=${city}`;

                fetch(geocodingUrl)
                    .then(response => response.json())
                    .then(data => {
                        if (data.length > 0) {
                            // Get the latitude and longitude from the geocoding data
                            latitude = data[0].lat;
                            longitude = data[0].lon;

                            // Initialize the Windy map with the retrieved coordinates
                            windyAPI.map.setView([latitude, longitude], 10);
                            L.popup()
                            .setLatLng([latitude, longitude])
                            .setContent(city)
                            .openOn(map);
                        } else {
                            alert('Location not found. Please enter a valid city name.');
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching geocoding data:', error);
                    });
            });
        });
    }

    // Call the initialization function when the document is ready
    initWindyMap();

    // Update the Windy map's size on window resize
    window.addEventListener('resize', () => {
        const windyMap = document.getElementById('windy');
    });
});





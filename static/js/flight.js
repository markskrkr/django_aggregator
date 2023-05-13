$(document).ready(function() {
    $("#flight-search-form").submit(function(event) {
        event.preventDefault();

        var departure = $("#departure").val();
        var destination = $("#destination").val();
        var departureTime = $("#departure-time").val();

        $.ajax({
            url: 'http://localhost:8000/flight_api/',
            type: 'GET',
            data: {
                departure_airport: departure,
                destin_airport: destination,
                departure_time: departureTime,
            },
            success: function(data) {
                alert("success");
                var flightsData = data[0].flights; // Access the flights list in the first element of the data list
                var flightsTable = $("#flights-table tbody");

                // Clear the table
                flightsTable.empty();

                // Add each flight to the table
                for (var i = 0; i < flightsData.length; i++) {
                    var flight = flightsData[i];

                    flightsTable.append(
                        `<tr>
                            <td>${flight.flight_num}</td>
                            <td>${flight.dep_airport}</td>
                            <td>${flight.dest_airport}</td>
                            <td>${flight.dep_datetime}</td>
                            <td>${flight.arr_datetime}</td>
                            <td>Max: ${flight.max_seatbusi}, Occupied: ${flight.seatbusi_occupied}, Price: ${flight.seatbusi_price}</td>
                            <td>Max: ${flight.max_seatcoom}, Occupied: ${flight.seatcoom_occupied}, Price: ${flight.seatcoom_price}</td>
                            <td>Max: ${flight.max_seatfirst}, Occupied: ${flight.seatfirst_occupied}, Price: ${flight.seatfirst_price}</td>
                        </tr>`
                    );
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                alert('Error: aa' + textStatus + ' ' + errorThrown);
            }
        });
    });
});
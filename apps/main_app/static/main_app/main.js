$(document).ready(function(){
    $('#find_gps').submit(function(e){
        // CODE FOR THE HOMEPAGE 

        // GRABBING LIST OF TRAIL BASED ON INPUTED CITY
        e.preventDefault()
        city = $('#city').val()
        radius = $('#radius').val()
        results = $('#results').val()
        sort = $('#sort').val()
        rating = $('#rating').val()
        // GRABBING LONGITUDE AND LATITUTE OF CITY FROM GOOGLE GEOCODE
        $.ajax({
            url:`https://maps.googleapis.com/maps/api/geocode/json?address=${city}&key=AIzaSyDeou99RPTo-hepKxhu-HrRHiOHtv63Hbc`,
            success: function(serverResponse) {
                latitude = serverResponse['results']['0']['geometry']['location']['lat']
                longitude = serverResponse['results']['0']['geometry']['location']['lng']
                // GRABBING LIST OF TRAILS AROUND CITY FILTERED BY USER INPUT AND OUTPUTING TABLE OF RESULTS
                $.ajax({
                    url:`https://www.hikingproject.com/data/get-trails?lat=${latitude}&lon=${longitude}&maxDistance=10&maxResults=${results}&sort=${sort}&minStars=${rating}&key=200361825-aa4516a9a335d5a3db804f58f080edf7`,
                    success: function(serverResponse){
                        console.log('accessing hike api')
                        output = "<table class='table'><thead><th>Name</th><th>Difficulty</th><th>Length</th><th>Location</th><th>Summary</th></thead><tbody>"
                        for(let x=0; x < serverResponse.trails.length; x++){
                            output += "<tr><td>"+serverResponse.trails[x].name+"</td><td>"+serverResponse.trails[x].difficulty+"</td><td>"+serverResponse.trails[x].length+"</td><td>"+serverResponse.trails[x].location+"</td><td>"+serverResponse.trails[x].summary+"</td><td><a href='/trail/"+serverResponse.trails[x].id+"/addtrip'>+</a></td></tr>"
                        }
                        output += "</tbody></table>"
                        $('#placeholder').html(output)
                    }
                })
            }
        })
    });
    // CODE FOR ADDTRIP PAGE

    // GET AND SHOW DETAILED INFO ON TRAIL
    trail = $('#trail_id').val()
    $.ajax({
        url: `https://www.hikingproject.com/data/get-trails-by-id?ids=${trail}&key=200361825-aa4516a9a335d5a3db804f58f080edf7`,
        success: function(serverResponse){
            output = "<div class='container'><div><h1 style='display: inline-block; margin-right:70px;'>"+serverResponse.trails[0]['name']+"</h1><h5 style='display: inline-block;'>Rating: "+serverResponse.trails[0]['stars']+"</h5></div><div><h3 style='display: inline-block; margin-right:50px;'>Trail Status: "+serverResponse.trails[0]['conditionStatus']+"</h3><h3 style='display: inline-block;'>Location: "+serverResponse.trails[0]['location']+"</div><div class='row'><div class='col'><table class='table'><thead><th>HIGH</th><th>LOW</th></thead><tbody><tr><td>"+serverResponse.trails[0]['high']+" ft</td><td>"+serverResponse.trails[0]['low']+" ft</td></tr></tbody></table></div><div class='col'><table class='table'><thead><th>ASCENT</th><th>DESCENT</th></thead><tbody><tr><td>"+serverResponse.trails[0]['ascent']+" ft</td><td>"+serverResponse.trails[0]['descent']+" ft</td></tr></tbody></table></div></div></div>"
            $('#trail_info').html(output)
        }
    });
    // ALLOWS FOR SETTING OF OVERNIGHT TRIP
    $('#overnight').click(function(){
        output = "<div class='form-row'><div class='col'>Start Date: <input class='form-control' type='date' name='start' id='start'></div><div class='col'>End Date: <input class='form-control' type='date' name='end' id='end'></div></div><input type='hidden' name='overnight' value='1'>"
        $('#dateholder').html(output)
    });
});
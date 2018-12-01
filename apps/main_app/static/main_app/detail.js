$(document).ready(function(){
    trail = $('#trail_id').val()
    $.ajax({
        url : `https://www.hikingproject.com/data/get-trails-by-id?ids=${trail}&key=200361825-aa4516a9a335d5a3db804f58f080edf7`,
        success: function(serverResponse){
            console.log(serverResponse)
            output = "<div class='container'><div><h1 style='display: inline-block; margin-right:70px;'>"+serverResponse.trails[0]['name']+"</h1><h5 style='display: inline-block;'>Rating: "+serverResponse.trails[0]['stars']+"</h5></div><div><h3 style='display: inline-block; margin-right:50px;'>Trail Status: "+serverResponse.trails[0]['conditionStatus']+"</h3><h3 style='display: inline-block;'>Location: "+serverResponse.trails[0]['location']+"</div><div class='row'><div class='col'><table class='table'><thead><th>HIGH</th><th>LOW</th></thead><tbody><tr><td>"+serverResponse.trails[0]['high']+" ft</td><td>"+serverResponse.trails[0]['low']+" ft</td></tr></tbody></table></div><div class='col'><table class='table'><thead><th>ASCENT</th><th>DESCENT</th></thead><tbody><tr><td>"+serverResponse.trails[0]['ascent']+" ft</td><td>"+serverResponse.trails[0]['descent']+" ft</td></tr></tbody></table></div></div><hr><div><h2>Details</h2><h6>Location: "+serverResponse.trails[0]['location']+"</h6><h6>Length: "+serverResponse.trails[0]['length']+" miles</h6><h6><a href="+serverResponse.trails[0]['url']+">Go to Site</a></h6></div><div><h2>Conditions</h2><h6>"+serverResponse.trails[0]['conditionStatus']+"</h6><h6>"+serverResponse.trails[0]['conditionDetails']+"</h6><h6>Updated: "+serverResponse.trails[0]['conditionDate']+"</h6></div></div>"
            $('#trail_detail').html(output)
        }
    })
});
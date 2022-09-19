const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, function (data) {
$(document).ready(function(){
        $("#character").html(data.name);
	})
});

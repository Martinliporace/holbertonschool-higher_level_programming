$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data){
	const titulos = data.results;
	titulos.forEach(titulo => {
		$('ul#list_movies').append('<li>'+titulo.title+'</li>');

	});
});


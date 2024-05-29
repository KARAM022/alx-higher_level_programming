$('https://swapi-api.alx-tools.com/api/films/?format=json').get(function (data) {
    for (const film of data.results) {
        $('#list_movies').append('<li>' + film.title + '</li>');
    }
});
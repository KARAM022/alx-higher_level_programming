$('https://hellosalut.stefanbohacek.dev/?lang=fr').get(function (data) {
    $('#hello').text(data.hello);
});
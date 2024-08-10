const URL = "https://swapi-api.alx-tools.com/api/films/?format=json"

jQuery.ajax({
    url: URL,
    method: "GET",
}).done(function (data) {
    const list = data["results"].map((film) => "<li>" + film["title"] + "</li>" )
    $("UL#list_movies").append(list)
})
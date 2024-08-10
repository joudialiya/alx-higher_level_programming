const URL = "https://swapi-api.alx-tools.com/api/people/5/?format=json"

jQuery.ajax({
    url: URL,
    method: "GET",
}).done(function (data) {
    console.log(data)
    $("DIV#character").text(data["name"])
})
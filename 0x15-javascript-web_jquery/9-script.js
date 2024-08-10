let hello_string;

jQuery.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    method: "GET",
}).done(function (data) {
    hello_string = data["hello"]
    $("DIV#hello").append(hello_string)
})
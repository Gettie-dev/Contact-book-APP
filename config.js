let rootPath= "https://mysite.itvarsity.org/api/ContactBook/";
let apiKey= checkApikey();

function checkApikey(){
    if (!localStorage.getItem("apiKey")) {
        window.open("api-key.html", "_self");
        //index.html("config.js", "_self")
    }
    return localStorage.getItem("apiKey");
}
/*
 * Fetch from a given URL, then run the `callback` function
 * with the given JSON response as its input. 
 */
function gatherData(link, callback) {
    fetch(link).then((response) => (response.json()))
        .then((data) => {callback(data)});
}
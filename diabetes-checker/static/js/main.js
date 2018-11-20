$(function() {
    // return result if available on load
    $(window).on('load', function() {
        // get value of result from hidden input element
        let str_output = document.getElementById('output').value;
        // convert string to json
        let json_output = JSON.parse(str_output);
        // locate relevant json object 
        json_output = json_output["Results"]["output1"][0];

        // iterate through the object with key
        for (var key in json_output) {
            // get element from html with key id and set innerHTML
            document.getElementById(key).innerHTML = key + ": " + json_output[key];
        }
    });
});
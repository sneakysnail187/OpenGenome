'use strict';

const debug = document.getElementById("debug");
const csv = document.getElementById("fileInput");

csv.addEventListener("change", function() {
    if (csv.files.length > 0) {
        debug.textContent = "File Read";
    }
});





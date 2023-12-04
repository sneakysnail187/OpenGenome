'use strict';

const input = document.getElementById("input");
const preview = document.querySelector(".preview");

input.style.opacity = 0;

input.addEventListener("change", processData, false);

function processData(){
    while (preview.firstChild) {
        preview.removeChild(preview.firstChild);
    }
    
    const curFiles = input.files;
    if (curFiles.length === 0) {
        const para = document.createElement("p");
        para.textContent = "No file selected";
        preview.appendChild(para);
    } 
    else {
        const list = document.createElement("ol");
        preview.appendChild(list);
    
        for (const file of curFiles) {
            const listItem = document.createElement("li");
            const para = document.createElement("p");
            if (file.type == "text/csv") {
                para.textContent = `File name ${file.name}, file size ${returnFileSize(
                file.size,
            )}.`;
            const image = document.createElement("img");
            image.src = URL.createObjectURL(file);
    
            listItem.appendChild(image);
            listItem.appendChild(para);
            }
            else {
                para.textContent = `File name ${file.name}: Not a valid file type. Update your selection.`;
                listItem.appendChild(para);
            }
    
            list.appendChild(listItem);
        }
    }
}
const switcher = document.querySelector('.btn');
switcher.addEventListener('click', function(){
    document.body.classList.toggle('light-theme');
    document.body.classList.toggle('dark-theme');

    const className = document.body.className;
    if(className == "light-theme") {
        this.textContent ="Light";
    }
    else{
        this.textContent = "Dark";
    }
    
    console.log('current class name: ' + className);
});
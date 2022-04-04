var display1 = document.getElementById("caption1")
var display2 = document.getElementById("caption2");
var display3 = document.getElementById("caption3");
var currentDisplay = display1;
var images = {
    "display": "background: url(../static/assets/display.jpg); background-size: 100%; background-repeat: no-repeat;",
    "display2": "background: url(../static/assets/display2.jpg); background-size: 100%; background-repeat: no-repeat;",
    "display3": "background: url(../static/assets/display3.jpg); background-size: 100%; background-repeat: no-repeat;"
}
var imageContainer = document.getElementById("main-container");

function changeDisplayRight(){
    if(currentDisplay == display1){
        imageContainer.setAttribute("style", images["display"]);
        currentDisplay.classList.add("hidden");
        currentDisplay = display2;
        currentDisplay.classList.remove("hidden");
    }
    else if(currentDisplay == display2){
        currentDisplay.classList.add("hidden");
        currentDisplay = display3;
        currentDisplay.classList.remove("hidden");
        imageContainer.setAttribute("style", );
    }
    else{
        currentDisplay.classList.add("hidden");
        currentDisplay = display1;
        currentDisplay.classList.remove("hidden");
        imageContainer.setAttribute("style", );
    }
}
function changeDisplayLeft(){
    if(currentDisplay == display1){
        currentDisplay.classList.add("hidden");
        currentDisplay = display3;
        currentDisplay.classList.remove("hidden");
        imageContainer.setAttribute("style", "background: url(../static/assets/display.jpg); background-size: 100%; background-repeat: no-repeat;");
    }
    else if(currentDisplay == display2){
        currentDisplay.classList.add("hidden");
        currentDisplay = display1;
        currentDisplay.classList.remove("hidden");
        imageContainer.setAttribute("style", "background: url(../static/assets/display2.jpg); background-size: 100%; background-repeat: no-repeat;");    }
    else{
        currentDisplay.classList.add("hidden");
        currentDisplay = display2;
        currentDisplay.classList.remove("hidden");
        imageContainer.setAttribute("style", "background: url(../static/assets/display3.jpg); background-size: 100%; background-repeat: no-repeat;");    }
}

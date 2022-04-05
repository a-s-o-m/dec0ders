var display1 = document.getElementById("display1")
var display2 = document.getElementById("display2");
var display3 = document.getElementById("display3");
var currentDisplay = display1;

function changeDisplayRight(){
    if(currentDisplay == display1){
        currentDisplay.classList.add("hidden");
        currentDisplay = display2;
        currentDisplay.classList.remove("hidden");
    }
    else if(currentDisplay == display2){
        currentDisplay.classList.add("hidden");
        currentDisplay = display3;
        currentDisplay.classList.remove("hidden");
    }
    else{
        currentDisplay.classList.add("hidden");
        currentDisplay = display1;
        currentDisplay.classList.remove("hidden");
    }
}
function changeDisplayLeft(){
    if(currentDisplay == display1){
        currentDisplay.classList.add("hidden");
        currentDisplay = display3;
        currentDisplay.classList.remove("hidden");
    }
    else if(currentDisplay == display2){
        currentDisplay.classList.add("hidden");
        currentDisplay = display1;
        currentDisplay.classList.remove("hidden");
    }
    else{
        currentDisplay.classList.add("hidden");
        currentDisplay = display2;
        currentDisplay.classList.remove("hidden");
    }
}

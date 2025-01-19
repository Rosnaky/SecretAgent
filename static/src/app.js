console.log("abc");
let detectUrl = document.querySelector("#detect-url");
let detectBtn = document.querySelector("#detect-btn");
let detectedStatus = document.querySelector("#detected-status");

function setup() {
    detectedStatus.innerHTML = "Idle -- No scanning queried"
}

detectBtn.addEventListener("click", function() {
    console.log("Scanning...");
    detectedStatus.innerHTML = "Scanning... (x%)";
    try {     
        window.location.replace("/app.html?")
    } catch(err) {
        console.error(`Error: ${err}`);
        detectedStatus.innerHTML = "An HTTP error occurred";
    }
});

setup();
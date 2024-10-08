
function showContent() {
    document.getElementById("arrowcontent").style.display = "block";
    document.getElementById("showBtn").style.display = "none";
    document.getElementById("hideBtn").style.display = "block";
    document.getElementById("hideBtn").style.textAlign = "center";
}

function hideContent() {
    document.getElementById("arrowcontent").style.display = "none";
    document.getElementById("showBtn").style.display = "block";
    document.getElementById("showBtn").style.textAlign = "center";
    document.getElementById("hideBtn").style.display = "none";
}


function setCookie(name, value, days) {
    const d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + d.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
    const cname = name + "=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(cname) === 0) {
            return c.substring(cname.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    const disclaimerAgreed = getCookie("disclaimerAgreed");
    const disclaimerModal = document.getElementById("disclaimer-modal");
    const body = document.body;

    if (disclaimerAgreed === "true") {
        disclaimerModal.style.display = "none";
        body.classList.remove("disabled");
    } else {
        disclaimerModal.style.display = "block";
        body.classList.add("disabled");
    }
}

function agreeDisclaimer() {
    setCookie("disclaimerAgreed", "true", 30);
    const disclaimerModal = document.getElementById("disclaimer-modal");
    const body = document.body;

    disclaimerModal.style.display = "none";
    body.classList.remove("disabled");
}
function read(value) {
    if (value === 'more') {
        document.getElementById("more").style.display = "";
        document.getElementById("moreBtn").style.display = "none";
    }
    if (value === "less") {
        document.getElementById("more").style.display = "none";
        document.getElementById("moreBtn").style.display = "";
    }

}

function read2(value) {
    if (value === 'more') {
        document.getElementById("more2").style.display = "";
        document.getElementById("moreBtn2").style.display = "none";
    }
    if (value === "less") {
        document.getElementById("more2").style.display = "none";
        document.getElementById("moreBtn2").style.display = "";
    }

}
document.addEventListener('DOMContentLoaded', function () {
    var rewardContainer = document.querySelector('.reward-container3');
    var contentDivs = document.querySelectorAll('.reward-content3');
    let currentIndex = 0;

    function changeContent(direction) {
        var totalItems = contentDivs.length;
        var itemWidth = contentDivs[0].offsetWidth + parseInt(window.getComputedStyle(contentDivs[0]).marginRight);

        if (direction === 'left3') {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalItems - 1;
        } else if (direction === 'right3') {
            currentIndex = (currentIndex < totalItems - 1) ? currentIndex + 1 : 0;
        }

        var translateX = -currentIndex * itemWidth;
        rewardContainer.style.transform = 'translateX(' + translateX + 'px)';
    }

    document.querySelector('.btn-left3').addEventListener('click', function () {
        changeContent('left3');
    });

    document.querySelector('.btn-right3').addEventListener('click', function () {
        changeContent('right3');
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var rewardContainer = document.querySelector('.reward-container2');
    var contentDivs = document.querySelectorAll('.reward-content2');
    let currentIndex = 0;

    function changeContent(direction) {
        var totalItems = contentDivs.length;
        var itemWidth = contentDivs[0].offsetWidth + parseInt(window.getComputedStyle(contentDivs[0]).marginRight);

        if (direction === 'left2') {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalItems - 1;
        } else if (direction === 'right2') {
            currentIndex = (currentIndex < totalItems - 1) ? currentIndex + 1 : 0;
        }

        var translateX = -currentIndex * itemWidth;
        rewardContainer.style.transform = 'translateX(' + translateX + 'px)';
    }

    document.querySelector('.btn-left2').addEventListener('click', function () {
        changeContent('left2');
    });

    document.querySelector('.btn-right2').addEventListener('click', function () {
        changeContent('right2');
    });
});

window.addEventListener('scroll', function () {
    var navbar = document.getElementById('aboutus');
    if (window.scrollY > 80) {
        navbar.style.background="black";
    } else {
        navbar.style.background="none";
    }
});

function updateFlag() {
    var select = document.getElementById("countryName");
    var selectedOption = select.options[select.selectedIndex];
    var flagSrc = selectedOption.getAttribute("data-flag-src");
    var countryCode = selectedOption.getAttribute("data-country-code");

    document.getElementById("countryFlagSymbol").src = flagSrc;
    document.getElementById("countryCode").innerText = countryCode;
}




document.addEventListener('DOMContentLoaded',function(){
    const managementBtn=document.getElementById('managementBtn');
    managementBtn.addEventListener('click',function(){
        document.getElementById('management-view').style.display="block";
        document.getElementById('committees-view').style.display="none";
        document.getElementById('management-view2').style.display="block";
        document.getElementById('committees-view2').style.display="none";
    });

    const committeesBtn=document.getElementById('committeesBtn');
    committeesBtn.addEventListener('click',function(){
        document.querySelector('#management-view').style.display="none";
        document.querySelector('#committees-view').style.display="block";
        document.querySelector('#management-view2').style.display="none";
        document.querySelector('#committees-view2').style.display="block";
    });

});

/*--------------------------------------------Canvas desing----------------------------------------------------------------*/
document.addEventListener("DOMContentLoaded", function() {
    var currentIndex = 0;
    var canvasCards = document.querySelectorAll('.canvasCard');
    
    function showCanvasCard(index) {
        canvasCards.forEach(function(card, i) {
            card.classList.toggle('active', i === index);
        });
    }

    document.querySelector('.btn-left4').addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : canvasCards.length - 1;
        showCanvasCard(currentIndex);
    });

    document.querySelector('.btn-right4').addEventListener('click', function() {
        currentIndex = (currentIndex < canvasCards.length - 1) ? currentIndex + 1 : 0;
        showCanvasCard(currentIndex);
    });

    // Initially show the first canvas card
    showCanvasCard(currentIndex);
});

// Function to draw on a canvas
function drawOnCanvas(canvasId) {
    var canvas = document.getElementById(canvasId);
    if (canvas) {
        var ctx = canvas.getContext('2d');
        // Begin a new path
        ctx.beginPath();
        ctx.moveTo(125, 75);    // Starting point
        ctx.lineTo(175, 75);   // Draw a line to (175, 75)
        ctx.lineTo(150, 75);   // Draw a line to (150, 75)
        ctx.lineTo(150, 50);   // Draw a line to (150, 50)
        ctx.lineTo(500, 50);   // Draw a line to (500, 50)
        ctx.lineTo(500, 450);  // Draw a line to (500, 450)
        ctx.lineTo(50, 450);   // Draw a line to (50, 450)
        ctx.strokeStyle = 'red';
        ctx.stroke();
    }
}

// Call the drawOnCanvas function for each canvas
drawOnCanvas('myCanvas1');
drawOnCanvas('myCanvas2');
// Add more drawOnCanvas calls as needed for additional canvases

/*---------------------------------------------------Finance page -------------------------------------------------------*/



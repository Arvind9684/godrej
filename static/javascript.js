// -----------------------------------------------------------Filter Function build------------------------------------------------------

// ---------------------------------------------index JS-------------------------------------------------------

function nameValidation(name) {
    // Regular expression to match strings with only letters and spaces and at least one vowel
    var nameExp = new RegExp(/^[A-Za-z\s]*[AEIOUaeiou][A-Za-z\s]*$/);
    // Check if the name matches the regular expression and has at least 2 characters
    if (name.value.length > 2 && name.value.match(nameExp)) {
        name.style.border="";
    }
    else{
        alert("Name must be at least 2 characters long, contain only letters and spaces, and include at least one vowel.");
        name.style.border="1px solid red";
        return false;
    }
    return true;
}



function mobileValidation(mobile) {
    // Mobile number should be 10 digits long and should contain only numbers
    var mobilePattern = /^[0-9]{10}$/;
    if (!mobilePattern.test(mobile.value)) {
        alert("Mobile number must be 10 digits long.");
        mobile.style.border="1px solid red";
        return false;
    }
    mobile.style.border="";
    return true;
}

function emailValidation(email) {
    // Basic email pattern validation
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email.value)) {
        alert("Please enter a valid email address.");
        return false;
    }
    email.style.border="";
    return true;
}

function validateform() {
    var name = document.getElementById('name');
    var mobile = document.getElementById('mobile');
    var email = document.getElementById('email');

    var nameVal = nameValidation(name);
    var mobileVal = mobileValidation(mobile);
    var emailVal = emailValidation(email);

    if (nameVal && mobileVal && emailVal) {
        return true;
    }
    else{
        return false;
    }
    return false;
}

// ---------------------------------------------------------------------------------------------------------------
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
        function setCookie(name, value, days) {
            let expires = "";
            if (days) {
                const date = new Date();
                date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Convert days to milliseconds
                expires = "; expires=" + date.toUTCString(); // Set expiration time
            }
            document.cookie = name + "=" + (value || "") + expires + "; path=/";
        }
        // Usage example: Set a cookie named "visit_csrf" with the value "123456" that expires in 7 days
        setCookie("visiter_csrf",getCookie('csrftoken'), 7);
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

/*---------------------------------------------------chatboat -------------------------------------------------------*/
function submitData(data) {
    fetch('/chatbot-data/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {
        if (result.status === 'success') {
            // Redirect to a new page to display the data
            window.location.href = `/chatbot-result/${result.id}/`;
        } else {
            console.error('Error submitting data:', result.message);
        }
    })
    .catch(error => {
        console.error('Fetch error:', error);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const chatbotBody = document.getElementById('chatbot-body');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const chatbotClose = document.getElementById('chatbot-close');

    const steps = [
        { question: 'What is your name?', field: 'name' },
        { question: 'What is your mobile number?', field: 'mobile' },
        { question: 'What is your email address?', field: 'email' },
    ];

    let currentStep = 0;
    const userData = {};

    function showMessage(message, isBot = true) {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = message;
        messageDiv.style.marginBottom = '10px';
        messageDiv.style.padding = '5px';
        messageDiv.style.backgroundColor = isBot ? '#e9ecef' : '#007bff';
        messageDiv.style.color = isBot ? '#000' : '#fff';
        chatbotBody.appendChild(messageDiv);
        chatbotBody.scrollTop = chatbotBody.scrollHeight;
    }

    function startChat() {
        showMessage(steps[currentStep].question);
    }

    function handleInput() {
        const userResponse = userInput.value.trim();
        if (userResponse) {
            userData[steps[currentStep].field] = userResponse;
            
            // Show user response
            showMessage(`You: ${userResponse}`, false);

            userInput.value = '';

            if (currentStep < steps.length - 1) {
                currentStep++;
                showMessage(steps[currentStep].question);
            } else {
                showMessage('Thank you! Here is the data you provided:');
                showMessage(`Name: ${userData.name}`);
                showMessage(`Mobile: ${userData.mobile}`);
                showMessage(`Email: ${userData.email}`);
                showMessage('Your data has been submitted.');
                userInput.style.display="none";
                sendBtn.style.display="none";
                submitData(userData);
            }
        }
    }

    function submitData(data) {
        fetch('/chatbot-data/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(result => {
            if (result.status === 'success') {
                console.log('Data submitted successfully');
            } else {
                console.error('Error submitting data:', result.message);
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
        });
    }

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [cookieName, cookieValue] = cookie.split('=');
            if (cookieName.trim() === name) {
                return cookieValue;
            }
        }
        return null;
    }

    sendBtn.addEventListener('click', handleInput);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            handleInput();
        }
    });

    chatbotClose.addEventListener('click', () => {
        document.getElementById('chatbot-container').style.display = 'none';
    });

    startChat();
});









document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById("disclamerBtn");
    const content = document.getElementById("Disclamer-content2");
    const icon = document.querySelector("#disclamerShowBtn i");

    btn.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior

        if (content.classList.contains('disclamer-show')) {
            content.style.display="none";
            content.classList.remove('disclamer-show')
            content.classList.add('disclamer-hide')
            icon.classList.remove('bi-caret-down-fill');
            icon.classList.add('bi-caret-right-fill');
        } else {
            content.classList.remove('disclamer-hide')
            content.classList.add('disclamer-show')
            content.style.display="";
            icon.classList.remove('bi-caret-right-fill');
            icon.classList.add('bi-caret-down-fill');
        }
    });
});


function subscribe() {
    // Function to handle the subscription logic
    closeModal();
}

function closeModal() {
    document.getElementById('subscription').style.display = 'none';
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('subscription').style.display = 'block';
});


$(document).ready(function(){
    $('#getOtpBtnmobile').click(function(){
        $('#loginModal').modal('show');
    });

    $('#continueWithEmailBtn').click(function(){
        $('#email').show();
        $('#mobile').hide();
    });

    $('#getOtpBtnEmail').click(function(){
        var email = $('#email').val();
        var terms = $('#terms').is(':checked');

        if (!terms) {
            alert('You must agree to the terms and conditions.');
            return;
        }

        if (email === '') {
            alert('Please enter your email address.');
            return;
        }

        var data = {
            email: email,
            terms: terms
        };

        $.ajax({
            url: '/path-to-your-server-endpoint',
            type: 'POST',
            data: data,
            success: function(response) {
                // Handle success
                alert('OTP sent to your email.');
            },
            error: function(xhr, status, error) {
                // Handle error
                alert('An error occurred: ' + error);
            }
        });
    });
});

function updateAdminUserType(userType) {
    if (userType === 'customer') {
        
        $('#customerloginForm').show();
        $('#employeeloginForm').hide();
    } else {
       
        $('#customerloginForm').hide();
        $('#employeeloginForm').show();
    }
}

function close_admin_login_form() {
    $('#loginModal').modal('hide');
}

function updateFlag() {
    var selectedCountry = $('#countryName option:selected');
    var flagSrc = selectedCountry.data('flag-src');
    $('#countryFlagSymbol').attr('src', flagSrc);
}
function continuewithemail(){
    document.getElementById('email').style.display="block";
    document.getElementById('mobile').style.display="none";
    var getOtpBtn=document.getElementById('getOtpBtnmobile');
    getOtpBtn.innerHTML="Get OTP on E-mail"
    var formAction=document.getElementById('customerloginForm');
    formAction.action="sendEmail";
    var continuewidthBtn = document.getElementById('continueWithEmailBtn');
    continuewidthBtn.innerHTML = "Continue with Mobile";
    continuewidthBtn.onclick = continuewithemobile;
}

function continuewithemobile(){
    document.getElementById('email').style.display="none";
    document.getElementById('mobile').style.display="block";
    var getOtpBtn=document.getElementById('getOtpBtnmobile');
    getOtpBtn.innerHTML="Get OTP on Mobile"
    var formAction=document.getElementById('customerloginForm');
    formAction.action="sendMobile";
    var continuewidthBtn = document.getElementById('continueWithEmailBtn');
    continuewidthBtn.innerHTML = "Continue with E-mail";
    continuewidthBtn.onclick = continuewithemail;
}


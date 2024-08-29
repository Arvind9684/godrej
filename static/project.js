
function viewsOption(value) {
    const val1 = value;

    if (val1 === "list") {
        var listContainers = document.getElementsByClassName("container-list");
        var mapContainers = document.getElementsByClassName("container-map");
        var listviews=document.getElementById("listviews");
        var mapviews=document.getElementById("mapviews");

        listviews.style.fontWeight="bold";
        listviews.style.textDecoration="underline";
        mapviews.style.fontWeight="normal";
        mapviews.style.textDecoration="none";


        // Display list containers and hide map containers
        for (var i = 0; i < listContainers.length; i++) {
            listContainers[i].style.display = "block";
        }
        for (var j = 0; j < mapContainers.length; j++) {
            mapContainers[j].style.display = "none";
            
        }
        
    }

    if (val1 === "map") {
        var listContainers = document.getElementsByClassName("container-list");
        var mapContainers = document.getElementsByClassName("container-map");
        var listviews=document.getElementById("listviews");
        var mapviews=document.getElementById("mapviews");

        listviews.style.fontWeight="normal";
        listviews.style.textDecoration="none";
        mapviews.style.fontWeight="bold";
        mapviews.style.textDecoration="underline";


        // Display map containers and hide list containers
        for (var i = 0; i < listContainers.length; i++) {
            listContainers[i].style.display = "none";
        }
        for (var j = 0; j < mapContainers.length; j++) {
            mapContainers[j].style.display = "block";
            initMap();
        }
    }
}

// Function to update the display value
function updateValue(value) {
    const output = document.getElementById('rangeValue');
    output.innerText = value;

    const rows = document.querySelectorAll(".card");
    rows.forEach(row => {
        const cells = row.querySelectorAll('.price');
        let matches = false;

        cells.forEach(cell => {
            if (parseInt(cell.textContent) <= parseInt(value)) {
                matches = true;
            }
        });

        if (matches) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}



function updateCheckboxCount() {
    const checkboxes = document.querySelectorAll('.cities-checkbox');
    const checkedCount = Array.from(checkboxes).filter(checkbox => checkbox.checked).length;
    document.getElementById('citycount').innerText = checkedCount;
    const checkedValues = Array.from(document.querySelectorAll('.cities-checkbox:checked')).map(cb => cb.value.toLowerCase());
    const rows = document.querySelectorAll('.card');

    if (checkedValues.length === 0) {
        // If no checkboxes are checked, show all rows
        rows.forEach(row => {
            row.style.display = '';
        });
    } else {
        // Otherwise, filter rows based on checked checkboxes
        rows.forEach(row => {
            const cells = row.querySelectorAll('p');
            let matches = false;

            cells.forEach(cell => {
                checkedValues.forEach(value => {
                    if (cell.textContent.toLowerCase().includes(value)) {
                        matches = true;
                    }
                });
            });

            if (matches) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }
}


function updateCommercialValue(value) {
    const filterInput = value; // Assuming `value` is the input value
    const filterValue = filterInput.toLowerCase(); // Use parentheses to call the function
    const rows = document.querySelectorAll('.card');
    
    rows.forEach(row => {
    const cells = row.querySelectorAll('.environmenttype');
    let matches = false;
    cells.forEach(cell => {
        if (cell.textContent.toLowerCase().includes(filterValue)) {
            matches = true;
        }
    });

    if (matches) {
        row.style.display = '';
    } else {
        row.style.display = 'none';
    }
}); 
}


document.addEventListener("DOMContentLoaded", function() {
    const filterInput = document.getElementById('filterInput');
    filterInput.addEventListener('keyup', function() {
        const filterValue = filterInput.value.toLowerCase();
        const rows = document.querySelectorAll('.card');
        rows.forEach(row => {
            
            const cells = row.querySelectorAll('h4');
            let matches = false;

            cells.forEach(cell => {
                if (cell.textContent.toLowerCase().includes(filterValue)) {
                    matches = true;
                }
            });

            if (matches) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
    
    filterInput.addEventListener('change',function(){
        const visit_csrf=getCookie("visiter_csrf");
        fetch('/search_history/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ filter:filterInput.value,csrftoken:visit_csrf }), // Correctly format the data
        })
    });

    const selectCountry = document.getElementById("selectCountry");
    selectCountry.addEventListener('change', function() {
        var countryData = selectCountry.value;
        var countryArr = JSON.parse(countryData);
        // alert("Country: " + countryArr[0] + "\nFlag URL: " + countryArr[1] + "\nCode: " + countryArr[2]);

        // Update the flag image and other elements
        document.getElementById("countryFlag").src = countryArr[2];
        document.getElementById("countryName").innerText = countryArr[0];
        document.getElementById("countryCode").value ="+"+countryArr[1];
    });

    const switchCheck = document.getElementById('flexSwitchCheckDefault');
    switchCheck.addEventListener('change', function() {
        if (this.checked) {
            const filterValue = "new launch";
            const rows = document.querySelectorAll('.card');
            
            rows.forEach(row => {
                const cells = row.querySelectorAll('.status');
                let matches = false;
                cells.forEach(cell => {
                    if (cell.textContent.toLowerCase().includes(filterValue)) {
                        matches = true;
                    }
                });

                if (matches) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        } 
        else {
            const rows = document.querySelectorAll('.card');
            rows.forEach(row => {
                
                    row.style.display = '';
            });
        
        }
    });
    
});
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
window.addEventListener('scroll', function () {
    var navbar = document.getElementById('investor');
    if (window.scrollY >90) {
        navbar.style.background="linear-gradient(to bottom, #8a8886, #fcf9f9)";
    } else {
        navbar.style.background="none";
    }
});
document.addEventListener('DOMContentLoaded', function () {
    const showMoreBtn = document.getElementById('show-more-btn');
    const showLessBtn = document.getElementById('show-less-btn');
    const showMoreBtn2 = document.getElementById('show-more-btn2');
    const showLessBtn2 = document.getElementById('show-less-btn2');
    const showMoreBtn3 = document.getElementById('show-more-btn3');
    const showLessBtn3 = document.getElementById('show-less-btn3');
    const showMoreBtn4 = document.getElementById('show-more-btn4');
    const showLessBtn4 = document.getElementById('show-less-btn4');
    const showMoreBtn5 = document.getElementById('show-more-btn5');
    const showLessBtn5 = document.getElementById('show-less-btn5');
    const showMoreBtn6 = document.getElementById('show-more-btn6');
    const showLessBtn6 = document.getElementById('show-less-btn6');
    const showMoreBtn7 = document.getElementById('show-more-btn7');
    const showLessBtn7 = document.getElementById('show-less-btn7');
    const showMoreBtn8 = document.getElementById('show-more-btn8');
    const showLessBtn8 = document.getElementById('show-less-btn8');
    const showMoreBtn9 = document.getElementById('show-more-btn9');
    const showLessBtn9 = document.getElementById('show-less-btn9');
    const showMoreBtn10 = document.getElementById('show-more-btn10');
    const showLessBtn10 = document.getElementById('show-less-btn10');
    if (showMoreBtn) {
        showMoreBtn.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn.style.display = 'none';
            showLessBtn.style.display="";
        });
    }
    if(showLessBtn){
        showLessBtn.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn.style.display = '';
            showLessBtn.style.display="none";

        })
    }
    if (showMoreBtn2) {
        showMoreBtn2.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row2');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn2.style.display = 'none';
            showLessBtn2.style.display="";
        });
    }
    if(showLessBtn2){
        showLessBtn2.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row2');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn2.style.display = '';
            showLessBtn2.style.display="none";

        })
    }

    if (showMoreBtn3) {
        showMoreBtn2.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row3');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn3.style.display = 'none';
            showLessBtn3.style.display="";
        });
    }
    if(showLessBtn3){
        showLessBtn3.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row3');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn3.style.display = '';
            showLessBtn3.style.display="none";

        })
    }

    if (showMoreBtn4) {
        showMoreBtn4.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row4');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn4.style.display = 'none';
            showLessBtn4.style.display="";
        });
    }
    if(showLessBtn4){
        showLessBtn4.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row4');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn4.style.display = '';
            showLessBtn4.style.display="none";

        })
    }

    if (showMoreBtn5) {
        showMoreBtn5.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row5');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn5.style.display = 'none';
            showLessBtn5.style.display="";
        });
    }
    if(showLessBtn5){
        showLessBtn5.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row5');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn5.style.display = '';
            showLessBtn5.style.display="none";

        })
    }
    if (showMoreBtn6) {
        showMoreBtn6.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row6');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn6.style.display = 'none';
            showLessBtn6.style.display="";
        });
    }
    if(showLessBtn6){
        showLessBtn6.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row6');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn6.style.display = '';
            showLessBtn6.style.display="none";

        })
    }

    if (showMoreBtn7) {
        showMoreBtn7.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row7');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn7.style.display = 'none';
            showLessBtn7.style.display="";
        });
    }
    if(showLessBtn7){
        showLessBtn7.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row7');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn7.style.display = '';
            showLessBtn7.style.display="none";

        })
    }

    if (showMoreBtn8) {
        showMoreBtn8.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row8');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn8.style.display = 'none';
            showLessBtn8.style.display="";
        });
    }
    if(showLessBtn8){
        showLessBtn8.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row8');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn8.style.display = '';
            showLessBtn8.style.display="none";

        })
    }


    if (showMoreBtn9) {
        showMoreBtn9.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row9');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn9.style.display = 'none';
            showLessBtn9.style.display="";
        });
    }
    if(showLessBtn9){
        showLessBtn9.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row9');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn9.style.display = '';
            showLessBtn9.style.display="none";

        })
    }


    if (showMoreBtn10) {
        showMoreBtn10.addEventListener('click', function () {
            const hiddenRows = document.querySelectorAll('.hidden-row10');
            hiddenRows.forEach(row => {
                row.style.display = 'flex';
            });
            showMoreBtn10.style.display = 'none';
            showLessBtn10.style.display="";
        });
    }
    if(showLessBtn10){
        showLessBtn10.addEventListener('click',function(){
            const hiddenRows = document.querySelectorAll('.hidden-row10');
            hiddenRows.forEach(row => {
                row.style.display = 'none';
            });
            showMoreBtn10.style.display = '';
            showLessBtn10.style.display="none";

        })
    }
});
/*---------------------------------Finance-------------------------------*/
document.addEventListener('DOMContentLoaded', function () {
    var rewardContainer = document.querySelector('.reward-container5');
    var contentDivs = document.querySelectorAll('.reward-content5');
    let currentIndex = 0;

    function changeContent(direction) {
        var totalItems = contentDivs.length;
        var itemWidth = contentDivs[0].offsetWidth + parseInt(window.getComputedStyle(contentDivs[0]).marginRight);

        if (direction === 'left5') {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalItems - 1;
        } else if (direction === 'right5') {
            currentIndex = (currentIndex < totalItems - 1) ? currentIndex + 1 : 0;
        }

        var translateX = -currentIndex * itemWidth;
        rewardContainer.style.transform = 'translateX(' + translateX + 'px)';
    }

    document.querySelector('.btn-left5').addEventListener('click', function () {
        changeContent('left5');
    });

    document.querySelector('.btn-right5').addEventListener('click', function () {
        changeContent('right5');
    });
    // Automatic sliding
    setInterval(function () {
        changeContent('right5');
    }, 2000); // Change every 3 seconds
});

/*---------------------------------------Investor information---------------------------------------*/
function investorMenu(linkId) {
    var patternView = document.getElementsByClassName('pattern-content');
    var serviceView = document.getElementsByClassName('service-content');
    var contactView = document.getElementsByClassName('contact-content');
    var otherView = document.getElementsByClassName('other-content');
    
    // Convert HTMLCollection to an array and apply the style change
    Array.from(patternView).forEach(function(element) {
        element.style.display = "none";
    });
    Array.from(serviceView).forEach(function(element) {
        element.style.display = "none";
    });
    Array.from(contactView).forEach(function(element) {
        element.style.display = "none";
    });
    Array.from(otherView).forEach(function(element) {
        element.style.display = "none";
    });
    viewlinkId=linkId+"-content";
    var viewContent=document.getElementsByClassName(viewlinkId)
    Array.from(viewContent).forEach(function(element) {
        element.style.display = "block";
    });
    // Remove active class from all nav links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.classList.remove('active');
    });

    // Add active class to the clicked nav link
    const selectedLink = document.getElementById(linkId);
    selectedLink.classList.add('active');
}
document.addEventListener('DOMContentLoaded', function() {
    const year = document.getElementById('year');
    const month = document.getElementById('month');

    function filterContent() {
        const selectedYear = year.value;
        const selectedMonth = month.value;
        const rows = document.querySelectorAll('.content');
        let match = false;

        rows.forEach(row => {
            const rowText = row.textContent;
            if (rowText.includes(selectedYear) && (selectedMonth === "" || rowText.toLowerCase().includes(selectedMonth))) {
                row.parentElement.style.display = "block";
                match = true;
            } else {
                row.parentElement.style.display = "none";
            }
        });

        if (!match) {
            console.log("No matches found for the selected filters");
        }
    }

    year.addEventListener('change', filterContent);
    month.addEventListener('change', filterContent);
});

function shownriloan(){
    var symbol=document.getElementById('symbol').innerHTML;
    var content=document.getElementById('homeloanricontent');
    if(symbol==="+"){
        content.style.display="";
        document.getElementById('symbol').innerHTML="-";
    }
    else if(symbol==="-"){
        content.style.display="none";
        document.getElementById('symbol').innerHTML="+";
    }
}

function eligiblereceive(){
    var symbol=document.getElementById('symbol2').innerHTML;
    var content=document.getElementById('eligiblereceive');
    if(symbol==="+"){
        content.style.display="";
        document.getElementById('symbol2').innerHTML="-";
    }
    else if(symbol==="-"){
        content.style.display="none";
        document.getElementById('symbol2').innerHTML="+";
    }

}

function propertydocs(){
    var symbol=document.getElementById('symbol3').innerHTML;
    var content=document.getElementById('propertydocs');
    if(symbol==="+"){
        content.style.display="";
        document.getElementById('symbol3').innerHTML="-";
    }
    else if(symbol==="-"){
        content.style.display="none";
        document.getElementById('symbol3').innerHTML="+";
    }

}

function additionaldocs(){
    var symbol=document.getElementById('symbol4').innerHTML;
    var content=document.getElementById('additionaldocs');
    if(symbol==="+"){
        content.style.display="";
        document.getElementById('symbol4').innerHTML="-";
    }
    else if(symbol==="-"){
        content.style.display="none";
        document.getElementById('symbol4').innerHTML="+";
    }

}

function representative(){
    var symbol=document.getElementById('symbol5').innerHTML;
    var content=document.getElementById('representative');
    if(symbol==="+"){
        content.style.display="";
        document.getElementById('symbol5').innerHTML="-";
    }
    else if(symbol==="-"){
        content.style.display="none";
        document.getElementById('symbol5').innerHTML="+";
    }

}

document.addEventListener('DOMContentLoaded',function(){
    var map = L.map('map').setView([20.5937, 78.9629], 3); // Center the map on India

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);

        // Fetch the location data from the server
        fetch("{% url 'getmap' %}")
            .then(response => response.json())
            .then(locations => {
                locations.forEach(function(location) {
                    L.marker([location.lat, location.lng]).addTo(map)
                        .bindPopup(location.name)
                        .openPopup();
                });
            });
});

        


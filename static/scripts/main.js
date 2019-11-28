// $(document).ready(function () {

//     $('#sidebarCollapse').on('click', function () {
//         $('#sidebar').toggleClass('active');
//     });

// });


function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}




// $(document).ready(function () {
//     // Collapse Navbar when the scroll is triggered
//     var navbarCollapse = function () {
//         if ($("#navMain").offset().top > 100) {
//             $("#navMain").addClass("navbar-shrink");
//         } else {
//             $("#navMain").removeClass("navbar-shrink");
//         }
//     };
//     // Collapse the nav bar if page is not at the top
//     navbarCollapse();
//     // Collapse the navbar when there is scroll activity
//     $(window).scroll(navbarCollapse);

//     $('.closeNav').click(function () {
//         document.getElementById("mySidenav").style.width = "0";
//     })

//     $('.openNav').click(function () {
//         document.getElementById('mySidenav').style.width = "290px";
//     })

// })
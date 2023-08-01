/*
Template Name: Nazox -  Admin & Dashboard Template
Author: Themesdesign
Contact: themesdesign.in@gmail.com
File: Session Timeout Js File
*/

$.sessionTimeout({
	keepAliveUrl: '/pages/utility/starter-page',
	logoutButton:'Logout',
	logoutUrl: '/account/logout/',
	redirUrl: '/pages/authentication/lock-screen',
	warnAfter: 3000,
	redirAfter: 30000,
	countdownMessage: 'Redirecting in {timer} seconds.'
});
document.getElementById("session-timeout-dialog-keepalive").removeAttribute("data-dismiss")
document.getElementById("session-timeout-dialog-keepalive").setAttribute("data-bs-dismiss", "modal");
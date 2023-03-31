$(".dropdown-trigger").dropdown();
$(document).ready(function () {
	setTimeout(function(){
        $("#messagesContainer").fadeOut( "slow" );
     }, 10000);
	$(".sidenav").sidenav();
});

var closeMessageContainer = function(){
    $("#messagesContainer").fadeOut( "fast" );
}

$("#closeMessagesIcon").on("click", ()=>{
	console.log("closing")
	closeMessageContainer();
});


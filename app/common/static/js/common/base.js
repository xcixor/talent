
$(document).ready(function () {
	$(".dropdown-trigger").dropdown();
	$(".sidenav").sidenav();
	setTimeout(function () {
		$("#messagesContainer").fadeOut("slow");
	}, 10000);
	$(".modal").modal({ dismissible: false });
	$(".hover-trigger").dropdown({
		hover: true,
		coverTrigger: false,
		constrainWidth: false,
		alignment:'center'
	});
});



var closeMessageContainer = function () {
	$("#messagesContainer").fadeOut("fast");
};

$("#closeMessagesIcon").on("click", () => {
	console.log("closing");
	closeMessageContainer();
});

$("#botLink").on("click", function () {
	// $(this).find("#botIcon").toggleClass("fa-message fa-xmark");
	console.log($(this).children());
	$(this).children().toggleClass("fa-message fa-xmark");
});

$(".dropdown-trigger").dropdown();
$(document).ready(function () {
	setTimeout(function () {
		$("#messagesContainer").fadeOut("slow");
	}, 10000);
	$(".modal").modal({ dismissible: false });
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

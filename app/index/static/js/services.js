
$(".card").hover(
	function () {
		$(this).find(".overlay").fadeIn(500);
	},
	function () {
		$(this).find(".overlay").fadeOut(500);
	}
);

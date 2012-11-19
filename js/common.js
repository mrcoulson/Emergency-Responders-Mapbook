$(document).ready(function() {
	$("#selNav").change(function() {
		if ($("#selNav").val() != "select") {
			window.location.href = $("#selNav").val();
		}
	});
	if ($("img[usemap]").length > 0) {
		$("img[usemap]").rwdImageMaps();
	}
});
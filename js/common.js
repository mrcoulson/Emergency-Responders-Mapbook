$(document).ready(function() {
	$("#selNav").change(function() {
		if ($("#selNav").val() != "select") {
			window.location.href = $("#selNav").val();
		}
	});
});
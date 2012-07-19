$(document).ready(function() {
	$("table tr:contains('Go to nav')").addClass("navRow");
	/*
	var urlQuery = location.search;
	urlQuery = urlQuery.replace('?', '');
	var split = urlQuery.split('=');
	// alert(split[1]);
	var backlink = $("a.backlink").attr("href");
	backlink = backlink + "?s=" + split[1];
	$("a.backlink").attr("href", backlink);
	*/
});

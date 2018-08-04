$(function() {

	// click button
	$("#predict").click(function(){
		console.log("I am clicked");

		// ajax call to predict
		$.post( "/predict", 
			{'fact': $("#fact").val()},
			function( data ) {
				var accusation = data.accusation;
				var term = data.term;
				$('#accusation').text("accusation: " + accusation);
				$('#term').text("term: " + term);
			});
	});
});

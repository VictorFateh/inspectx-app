$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
				message : $('#message').val()
			},
			type : 'POST',
			url : '/email'
		})
		.done(function(data) {

			if (data.error) {
				$('email-form').show();
				$('fail').show()
			    $('success').hide();
			}
			else {
			   $('email-form').hide();
			   $('success').show();
			   $('fail').hide();
			}

		});

		event.preventDefault();

	});

});
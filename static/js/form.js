$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
				car : $('#car').val(),
				location : $('#location').val(),
				date : $('#date').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				$('#title-start').hide();
				$('#title-error').show();
				$('#title-complete').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#scene').show();
				$('#errorAlert').hide();
				$('#inspection-form').hide();
				$('#title-start').hide();
				$('#title-error').hide();
				$('#title-complete').show();
			}

		});

		event.preventDefault();

	});

});
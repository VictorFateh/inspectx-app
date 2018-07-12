$(document).ready(function() {

    $.ajaxSetup({
        beforeSend:function() {
            $("#sendMessageButton").text("");
            $("#sendMessageButton").append('<div class="gauge-loader"></div>');
        },
        complete:function() {
            $("#sendMessageButton").text('Send');
        }
    });

	$('#email-form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
				message : $('#message').val()
			},
			type : 'POST',
			url : '/contact'
		})
		.done(function (data) {

			if (data.error) {
				$('#email-form').show();
				$('#fail').text(data.error).show();
			    $('#success').hide();
			    $('#car-animation').hide()
			}
			else {
			    $('#car-animation').show()
				$('#email-form').hide();
			   $('#success').text(data.response).show();
			   $('#fail').hide();
			}

		});

		event.preventDefault();

	});

});
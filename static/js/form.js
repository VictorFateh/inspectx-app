$(document).ready(function() {

    $.ajaxSetup({
        beforeSend:function() {
            $("#sendMessageButton").text("");
            $("#sendMessageButton").append('<div class="gauge-loader"></div>');
        },
        complete:function() {
            $("#sendMessageButton").text('Request Inspection');
        }
    });

    $('#datepicker').calendar({
    today: true,
    monthFirst: true
    });

	$('form').on('submit', function(event) {
	    document.getElementById("sendMessageButton")

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
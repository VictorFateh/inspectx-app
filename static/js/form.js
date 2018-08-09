$(document).ready(function() {

    var car_query = new CarQuery();
    car_query.init();
    car_query.initYearMakeModelTrim('car-years', 'car-makes', 'car-models', 'car-model-trims');
    car_query.initMakeModelTrimList('make-list', 'model-list', 'trim-list', 'trim-data-list');
    car_query.year_select_min=1990;
    car_query.year_select_max=2018;

    $.ajaxSetup({
        beforeSend:function() {
            $("#sendMessageButton").text("");
            $("#sendMessageButton").append('<div class="gauge-loader"></div>');
        },
        complete:function() {
            $("#sendMessageButton").text('Request Inspection');
        }
    });

    $('#date').datetimepicker({
                format: 'MM/DD/YYYY'
    });

    var placesAutocomplete = places({
        container: document.querySelector('#location'),
        type: 'city',
        aroundLatLngViaIP: false,
        countries: ['us'],
    });

	$('form').on('submit', function(event) {
	    document.getElementById("sendMessageButton")

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
                car : $('#car-years option:selected').text() + ' ' + $('#car-makes option:selected').text() + ' ' + $('#car-models option:selected').text() + ' ' + $('#car-model-trims option:selected').text(),
				location : $('#location').val(),
				service : 'Inspection',
				date : $('#date').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				$('#title-complete').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#scene').show();
				$('#errorAlert').hide();
				$('#inspection-form').hide();
				$('#title-start').hide();
				$('#title-complete').show();
			}

		});

		event.preventDefault();

	});
});
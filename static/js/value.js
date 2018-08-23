$(document).ready(function() {

    var car_query = new CarQuery();
    car_query.init();
    car_query.initYearMakeModelTrim('car-years', 'car-makes', 'car-models', 'car-model-trims');
    car_query.initMakeModelTrimList('make-list', 'model-list', 'trim-list', 'trim-data-list');

    $.ajaxSetup({
        beforeSend:function() {
            $("#valuation-submit").text("Loading...");
        },
        complete:function() {
            $("#valuation-submit").text('Schedule Valuation');
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
	    document.getElementById("valuation-submit")

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
                car : $('#car-years option:selected').text() + ' ' + $('#car-makes option:selected').text() + ' ' + $('#car-models option:selected').text() + ' ' + $('#car-model-trims option:selected').text(),
				location : $('#location').val(),
				service : 'Valuation',
				date : $('#date').val()
			},
			type : 'POST',
			url : '/value'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
				$('#val-info').show();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#scene').show();
				$('#errorAlert').hide();
				$('#value-form').hide();
				$('#val-info').hide();
			}

		});

		event.preventDefault();

	});
});
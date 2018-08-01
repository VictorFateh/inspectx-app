$(document).ready(function() {

     var carquery = new CarQuery();
     carquery.init();

     //Optional: initialize the year, make, model, and trim drop downs by providing their element IDs
     carquery.initYearMakeModelTrim('car-years', 'car-makes', 'car-models', 'car-model-trims');

     //Optional: set the onclick event for a button to show car data.
     $('#cq-show-data').click(  function(){ carquery.populateCarData('car-model-data'); } );

     //Optional: initialize the make, model, trim lists by providing their element IDs.
     carquery.initMakeModelTrimList('make-list', 'model-list', 'trim-list', 'trim-data-list');

     //Optional: set minimum and/or maximum year options.
     carquery.year_select_min=1990;
     carquery.year_select_max=2018;

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

	$('form').on('submit', function(event) {
	    document.getElementById("sendMessageButton")

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
                car : $('#car-years option:selected').text() + ' ' + $('#car-makes option:selected').text() + ' ' + $('#car-models option:selected').text() + ' ' + $('#car-model-trims option:selected').text(),
				location : $('#location').val(),
				service : 'PPI',
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
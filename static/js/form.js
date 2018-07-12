$(document).ready(function() {

    $('.popover-dismiss').popover({
        trigger: 'focus'
    })
    $('#poppy').popover({
        container: '#inspection-form'
    })

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
    disableMinute: true,
    today: true,
    monthFirst: true,
    closable: true,
    popupOptions: {
      position: 'top left',
      hideOnScroll: false
    }
    });

    var carquery = new CarQuery();
    carquery.init();
    carquery.setFilters( {sold_in_us:true} );
    carquery.initYearMakeModelTrim('car-years', 'car-makes', 'car-models', 'car-model-trims');
    carquery.initMakeModelTrimList('make-list', 'model-list', 'trim-list', 'trim-data-list');
    carquery.year_select_min=1980;
    carquery.year_select_max=2019;

	$('form').on('submit', function(event) {
	    document.getElementById("sendMessageButton")

		$.ajax({
			data : {
				name : $('#name').val(),
				email : $('#email').val(),
				phone : $('#phone').val(),
                car : ($('#car-years').val() + ' ' + $('#car-makes').val() + ' ' + $('#car-models').val() + ' ' + $('#car-model-trims option:selected').text()),
				location : $('#location').val(),
				service : $('#service').val(),
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
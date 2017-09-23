$(document).ready(function() {
    $('#calendar').fullCalendar({
         header: {
				left: 'prev,next today title',
				center: '',
				right: ''
        },
        views: {
            listMonth: {buttonText: 'list month'},
            listWeek: { buttonText: 'list week' }
        },
        contentHeight: 300,
        defaultView: 'listMonth',
        navLinks: true,
        eventLimit: true, // allow "more" link when too many events
        events: 'http://whatiswcs.com/rest/djcalendar/'
    })
});
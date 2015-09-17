var EventSource = require('eventsource');
 
var messageSource = new EventSource('http://127.0.0.1:9001/message-events');

messageSource.addEventListener(
    'added',
    function(event) {
    	console.log(event)
    },
    false
);


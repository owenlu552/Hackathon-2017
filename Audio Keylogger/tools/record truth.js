var truth = {
	'down': [],
	'up': []
};
$(document).on('keydown', (e) => truth.down.push({
		'key': e.key,
		't': e.timeStamp
	}));
$(document).on('keyup', (e) => truth.up.push({
		'key': e.key,
		't': e.timeStamp
	}));

$(document).ready(() => {
	function countdown(audio, light) {
		if (audio) {
			new Audio(audio + '.mp3').play();
		}
		if (light) {
			var $light = $('#' + light);
			$light.css('background-color', '').css('color', 'black');
			setTimeout(() => $light.css('background-color', 'gray').css('color', 'white'), 1000);
		} else {
			$('.countdown').html('');
		}
	};

	setTimeout(() => countdown('beep', 'red'), 1000);
	setTimeout(() => countdown('beep', 'yellow'), 2000);
	setTimeout(() => countdown('beep', 'green'), 3000);
	setTimeout(() => countdown('high beep', 'start'), 4000);
	setTimeout(() => countdown(null, null), 5000);
});

save = function() {
	function makeTextFile(text) {
		var data = new Blob([text], {
				type: 'text/plain'
			});

		// returns a URL you can use as a href
		return window.URL.createObjectURL(data);
	};

	var link = document.createElement('a');
	link.setAttribute('download', 'info.txt');
	link.href = makeTextFile(truth.down.map(e => e.key + ',' + e.t).join('\n'));
	link.dispatchEvent(new MouseEvent('click'));
};

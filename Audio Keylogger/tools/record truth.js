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
	function countdown(audio, count) {
		if (audio) {
			new Audio(audio + '.mp3').play();
		}
		$('#countdown').text(count);
	};

	setTimeout(() => countdown('beep', 3), 1000);
	setTimeout(() => countdown('beep', 2), 2000);
	setTimeout(() => countdown('beep', 1), 3000);
	setTimeout(() => countdown('high beep', 'Start!'), 4000);
	setTimeout(() => countdown(null, ''), 5000);
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

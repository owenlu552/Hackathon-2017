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

textFile = null;
makeTextFile = function(text) {
	var data = new Blob([text], {
			type: 'text/plain'
		});

	// If we are replacing a previously generated file we need to
	// manually revoke the object URL to avoid memory leaks.
	if (textFile !== null) {
		window.URL.revokeObjectURL(textFile);
	}

	textFile = window.URL.createObjectURL(data);

	// returns a URL you can use as a href
	return textFile;
};

save = function() {
	var link = document.createElement('a');
	link.setAttribute('download', 'info.txt');
	link.href = makeTextFile(truth.down.map(e => e.key + ',' + e.t).join('\n'));
	link.dispatchEvent(new MouseEvent('click'));
}

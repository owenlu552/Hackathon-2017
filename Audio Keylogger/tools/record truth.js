var truth = {
	"down": [],
	"up": []
};
$(document).on('keydown', (e) => truth.down.push({
	"key": e.key,
	"t": e.timeStamp
}));
$(document).on('keyup', (e) => truth.up.push({
	"key": e.key,
	"t": e.timeStamp
}));

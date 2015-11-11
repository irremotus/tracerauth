// tracer.js

var Tracer = function(canvas) {
	this.canvas = canvas;
	this.canvasOffset = this.canvas.offset();
	console.log(this.canvasOffset);

	this.ctx = this.canvas.get(0).getContext("2d");

	var ctx = this.ctx;
	ctx.rect(50, 50, this.canvas.width() - 100, this.canvas.height() - 100);
	ctx.stroke();

	this.points = [];

	function handleTouchStart(o) { return function(e) {
		e.preventDefault();

		this.points = [];
		console.log("Starting path");
	}};

	function handleTouchMove(o) { return function(e) {
		e.preventDefault();

		var t = (new Date()).getTime();

		var touch = e.targetTouches[0];
		var x = touch.pageX - o.canvasOffset.left;
		var y = touch.pageY - o.canvasOffset.top;

		o.points.push([x,y,t]);
		//console.log("pos (" + x.toString() + ", " + y.toString() + ")");
		var ctx = o.ctx;
		//ctx.fillStyle = "rgb(0,0,255)";
		ctx.fillRect(x, y, 1, 1);
	}};

	function handleTouchEnd(o) { return function(e) {
		e.preventDefault();

		console.log("Finished path");
	}};

	this.canvas.get(0).addEventListener("touchstart", handleTouchStart(this));
	this.canvas.get(0).addEventListener("touchmove", handleTouchMove(this));
	this.canvas.get(0).addEventListener("touchend", handleTouchEnd(this));
	
	console.log("created Tracer");
}

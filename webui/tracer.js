// tracer.js

var Tracer = function(canvas) {
	this.canvas = canvas;
	this.canvasOffset = this.canvas.offset();
	console.log(this.canvasOffset);

	this.ctx = this.canvas.get(0).getContext("2d");

	this.usetouch = false;

	this.drawShape = function() {
		var ctx = this.ctx;
		ctx.rect(100, 100, this.canvas.width() - 200, this.canvas.height() - 200);
		ctx.stroke();
	};
	this.drawShape();

	this.points = [];

	this.pathStart = function() {
		this.points = [];
		var ctx = this.ctx;
		ctx.clearRect(0, 0, this.canvas.width(), this.canvas.height());
		this.drawShape();
	};

	this.pathPoint = function(p) {
		this.points.push(p);
		//console.log("pos (" + x.toString() + ", " + y.toString() + ")");
		var ctx = this.ctx;
		//ctx.fillStyle = "rgb(0,0,255)";
		ctx.fillRect(p[0], p[1], 1, 1);
	};

	this.pathEnd = function() {
		
	};

	
	// Mouse handler methods

	function handleMouseStart(o) { return function(e) {
		e.preventDefault();

		o.pathStart();

		o.usetouch = false;

		console.log("Starting mouse path");
	}};

	function handleMouseMove(o) { return function(e) {
		e.preventDefault();

		if (e.buttons != 1) {
			return;
		}

		var t = (new Date()).getTime();

		var x = e.clientX - o.canvasOffset.left;
		var y = e.clientY - o.canvasOffset.top;

		o.pathPoint([x,y,t]);

	}};

	function handleMouseEnd(o) { return function(e) {
		e.preventDefault();

		o.pathEnd();

		console.log("Finished mouse path");
	}};

	
	// Touch handler methods
	
	function handleTouchStart(o) { return function(e) {
		e.preventDefault();

		o.pathStart();

		o.usetouch = true;

		console.log("Starting touch path");
	}};

	function handleTouchMove(o) { return function(e) {
		e.preventDefault();

		var t = (new Date()).getTime();

		var touch = e.targetTouches[0];
		var x = touch.pageX - o.canvasOffset.left;
		var y = touch.pageY - o.canvasOffset.top;

		o.pathPoint([x,y,t]);
	}};

	function handleTouchEnd(o) { return function(e) {
		e.preventDefault();

		o.pathEnd();

		console.log("Finished touch path");
	}};


	this.canvas.get(0).addEventListener("mousedown", handleMouseStart(this));
	this.canvas.get(0).addEventListener("mousemove", handleMouseMove(this));
	this.canvas.get(0).addEventListener("mouseup", handleMouseEnd(this));

	this.canvas.get(0).addEventListener("touchstart", handleTouchStart(this));
	this.canvas.get(0).addEventListener("touchmove", handleTouchMove(this));
	this.canvas.get(0).addEventListener("touchend", handleTouchEnd(this));
	
	console.log("Created Tracer");
}

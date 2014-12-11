function VisualzierContstructor() {
	out = {
		"settings": {
			"maxDay": 20, //24,
			"minDay": 8 //0
		},
		"data": null
	};

	out.init = function() {
		var that = this;
		d3.json("/galjsonsimp", function(error, json) {
			that.data = json;
			// this.generateCurrentTimeBar();
			// this.eachGallery();
			console.log(json)
			that.d3TimeGraph();
		});
	};

	out.hoursAndMinToFloat = function(time) {
		var splited = time.split(":");
		splited = (parseInt(splited[0]) + (parseInt(splited[1]) / 60))
		return splited
	};

	out.d3TimeGraph = function() {
		var that = this;
		this.updateCurTime();
		var day = this.settings.curDay,
			start = 24,
			end = 0,
			timeCovert = this.hoursAndMinToFloat;

		var max = d3.min(that.data, function(d) {
			return timeCovert(d["time"][day + "start"]);
		});
		var min = d3.max(that.data, function(d) {
			return timeCovert(d["time"][day + "end"]);
		});
		this.settings.maxDay = max;
		this.settings.minDay = min;

		var parent = d3.select("#gallerylist").append("ul")
		var listItems = parent.selectAll("li")
			.data(this.data)
			.enter()
			.append("li");

		listItems.append("div")
			.attr("class", "goodTimes")
			.style("left", function(d) {
				if (d["time"][day + "start"] == "None") {
					return 0;
				}
				var time = timeCovert(d["time"][day + "start"])
				return ((time - max) / min * 100) + "%";
			})
			.style("width", function(d) {
				if (d["time"][day + "start"] == "None") {
					return 0;
				}
				var startTime = timeCovert(d["time"][day + "start"])
				var endTime = timeCovert(d["time"][day + "end"])
				return ((endTime - startTime) / (min - max) * 100) + "%";
			})

		listItems.append("h3").text(function(d) {
			return d.gal;
		}).attr("class", "gallerytitle");
		listItems.append('h4').text(function(d) {
			return d.show || "-";
		}).attr("class", "showtitle");
		listItems.append("h4").text(function(d) {
			return d["time"][day + "start"].substring(0, 5) + " until " + d["time"][day + "end"].substring(0, 5)
		}).attr("class", "gallerytime");

		d3.select(".curtime .time-bar")
			.append("div")
			.attr("class", "curTime")
			.style("left", (out.settings.curTime / 24 * 100) + "%")

	}

	out.generateCurrentTimeBar = function() {
		this.updateCurTime();
		var parent = document.getElementById("current-time-bar");
		parent.innerHTML = "";

		var goodTimes = document.createElement("div"),
			curTime = document.createElement("div");

		goodTimes.style.left = (out.settings.minDay / 24 * 100) + "%";
		goodTimes.style.width = ((out.settings.maxDay - out.settings.minDay) / 24 * 100) + "%";
		goodTimes.className = "goodTimes";
		parent.appendChild(goodTimes);

		curTime.style.left = (out.settings.curTime / 24 * 100) + "%"
		curTime.className = "curTime";
		parent.appendChild(curTime);
	}

	out.eachGallery = function() {
		// var galleries = document.getElementsByClassName("gallery");
		// for(var a = 0, max = galleries.length; a<max; ++a){
		// 	console.log(galleries[a]);
		// }
	}


	out.updateCurTime = function() {
		var tempDate = new Date();
		this.settings.curTime = tempDate.getHours() + (tempDate.getMinutes() / 60);

		var day = tempDate.getDay();

		switch (day) {
			case 0:
				day = "sun_";
				break;
			case 1:
				day = "mon_";
				break;
			case 2:
				day = "tue_";
				break;
			case 3:
				day = "wed_";
				break;
			case 4:
				day = "thu_";
				break;
			case 5:
				day = "fir_";
				break;
			case 6:
				day = "sat_";
				break;
		}

		this.settings.curDay = day;
	};

	return out
}
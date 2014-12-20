function VisualzierContstructor() {
	out = {
		"settings": {
			"maxDay": 20, //24,
			"minDay": 8, //0
			"offsetoftime": 0,
			"timeOffSetEnable": true
		},
		"data": null
	};

	out.init = function() {
		var that = this;
		d3.json("/galjsonsimp", function(error, json) {
			that.data = json;
			// this.generateCurrentTimeBar();
			// this.eachGallery();
			that.d3TimeGraph();
			that.d3Options();
			that.mainNavSetup();
		});
	};

	out.mainNavSetup = function() {
		//TODO
		// SET UP the top nav HERE!

	}

	out.hoursAndMinToFloat = function(time) {
		var splited = time.split(":");
		splited = (parseInt(splited[0]) + (parseInt(splited[1]) / 60))
		return splited
	};

	out.removed3TimeGraph = function() {
		var parent = d3.select(".gallerygraph");
		if (!parent[0][0]) {
			return null;
		} else {
			parent.html("");
		}
		Map.resetMap()
	}

	out.d3TimeGraph = function(data) {
		var that = this;
		var locData = that.data;
		if (data) {
			locData = data;
		}
		this.updateCurTime();
		var day = this.settings.curDay,
			start = 24,
			end = 0,
			timeCovert = this.hoursAndMinToFloat;

		var max = d3.min(locData, function(d) {
			if (!d["time"][day + "start"]) {
				return false;
			}
			if (d["opening"]) {
				return timeCovert(d["opening"]["opening_start_time"]);
			}
			return timeCovert(d["time"][day + "start"]);
		});
		var min = d3.max(locData, function(d) {
			if (!d["time"][day + "end"]) {
				return false;
			}
			if (d["opening"]) {
				return timeCovert(d["opening"]["opening_end_time"]);
			}

			return timeCovert(d["time"][day + "end"]);
		});
		this.settings.maxDay = max;
		this.settings.minDay = min;

		// REMOVE THIS !@#$	@NASKGN AWIONT Q	@#NT ONzxcgvb
		// REMOVE THIS !@#$	@NASKGN AWIONT Q	@#NT ONzxcgvb
		out.settings.curTime = out.settings.curTime
		// REMOVE THIS !@#$	@NASKGN AWIONT Q	@#NT ONzxcgvb
		// REMOVE THIS !@#$	@NASKGN AWIONT Q	@#NT ONzxcgvb
		var offSetOfTime = 0;
		if (out.settings.timeOffSetEnable && out.settings.curTime < min && out.settings.curTime > max) {
			offSetOfTime = out.settings.curTime - max;
		}

		var parent = d3.select(".gallerygraph");
		if (!parent[0][0]) {
			parent = d3.select("#gallerylist").append("ul")
				.attr("class", "gallerygraph")
		}
		var listItems = parent.selectAll("li")
			.data(locData)
			.enter()
			.append("li")
			.append("a");

		listItems
			.attr("href", function(d) {
				return "/galinlineview/" + d.slug
			})
			.on("click", function() {
				d3.event.preventDefault();
				out.loadGallery(this.href);
				return false;
			})
			.append("div")
			.attr("class", function(d) {
				var out = "goodTimes";
				if (d["opening"]) {
					out += " opening";
				}
				return out;
			})
			.style("left", function(d) {
				if (!d["time"][day + "start"]) {
					return 0;
				}
				var startTime = d["time"][day + "start"]
				if (d["opening"]) {
					startTime = d["opening"]["opening_start_time"]
				}
				return ((timeCovert(startTime) - max - offSetOfTime) / (min - max) * 100) + "%";
			})
			.style("width", function(d) {
				if (!d["time"][day + "start"]) {
					return 0;
				}
				var startTime = timeCovert(d["time"][day + "start"]),
					endTime = timeCovert(d["time"][day + "end"]);
				if (d["opening"]) {
					startTime = timeCovert(d["opening"]["opening_start_time"]);
					endTime = timeCovert(d["opening"]["opening_end_time"]);
				}
				return ((endTime - startTime) / (min - max) * 100) + "%";
			})

		listItems.append("h3").text(function(d) {
			var description = d["time"][day + "start"].substring(0, 5) + " until " + d["time"][day + "end"].substring(0, 5)
			if (d["opening"]) {
				description = d["opening"]["opening_start_time"].substring(0, 5) + " until " + d["opening"]["opening_end_time"].substring(0, 5)
			}
			Map.addMarker(d.lat, d.log, d.gal, description);
			return d.gal;
		}).attr("class", "gallerytitle");

		listItems.append('h4').text(function(d) {
			if (d.show == "noshow") {
				return "no current show";
			}
			return d.show.title;
		}).attr("class", "showtitle");

		listItems.append("h4").text(function(d) {
			if (!d["time"][day + "start"]) {
				return "closed"
			}
			if (d["opening"]) {
				return d["opening"]["opening_start_time"].substring(0, 5) + " until " + d["opening"]["opening_end_time"].substring(0, 5)
			}
			return d["time"][day + "start"].substring(0, 5) + " until " + d["time"][day + "end"].substring(0, 5)
		}).classed({
			"gallerytime": true
		});

		var detailPanel = listItems.append("div").classed({
			"details": true
		})
		detailPanel.append("div").text("map")
			.classed({
				"gotoonmap": true
			})
			.on("click", function(d) {
				console.log(d)
				Map.move(d.lat, d.log);
				d3.event.stopPropagation();
				d3.event.preventDefault();
			});


		d3.select(".curtime .time-bar")
			.append("div")
			.classed({
				"curTime": true
			})
			.style("left", (out.settings.curTime / 24 * 100) + "%")
	}

	out.d3Options = function() {
		var parent = d3.select("#gallerylist").append("ul")
		parent.attr("class", "graphoptions")

		parent.append("li").append("a")
			.text("refresh")
			.attr("href", "#")
			.on("click", function(event) {
				out.removed3TimeGraph()
				out.d3TimeGraph();
			});
		parent.append("li").append("a")
			.text("time translate")
			.attr("href", "#")
			.on("click", function(event) {
				out.settings.timeOffSetEnable = !out.settings.timeOffSetEnable;
				out.removed3TimeGraph();
				out.d3TimeGraph();
			})
	}

	out.loadGallery = function(gallery) {
		$("#galleryinline").load(gallery, function(response, status, xhr) {
			$("#gallerycontainer").addClass("singlegalactive");
			$(".topblackbar").height($("#gallerynav").height());

			$(".closeinlinegal").click(function(event) {
				event.preventDefault();
				$("#gallerycontainer").removeClass("singlegalactive");
				$("#galleryinline").html("");
				return false;
			})
		});
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
				day = "fri_";
				break;
			case 6:
				day = "sat_";
				break;
		}

		this.settings.curDay = day;
	};

	return out
}
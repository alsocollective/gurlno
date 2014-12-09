function VisualzierContstructor() {
	out = {
		"settings": {
			"maxDay": 20, //24,
			"minDay": 8 //0
		},
		"data": null
	};

	out.init = function(data) {
		this.data = data;
		// this.generateCurrentTimeBar();
		// this.eachGallery();
		this.d3TimeGraph();
	};

	out.d3TimeGraph = function() {
		this.updateCurTime();
		var day = this.settings.curDay,
			start = 24,
			end = 0;



		var parent = d3.select("#gallerylist").append("ul")
		var listItems = parent.selectAll("li")
			.data(this.data)
			.enter()
			.append("li");

		listItems.append("h3").text(function(d) {
			return d.title;
		});
		listItems.append("div")
			.attr("class", "time-bar")
			.append("div")
			.attr("class", "goodTimes")
			.style("left", function(d) {
				if (d["time"][day][0] == "None") {
					return 0;
				}
				var splited = d["time"][day][0].split(":");
				splited = (parseInt(splited[0]) + (parseInt(splited[1]) / 60))
				if (splited < start) {
					start = splited;
				}
				return (splited / 24 * 100) + "%";
			})
			.style("width", function(d) {
				if (d["time"][day][0] == "None") {
					return 0;
				}
				var splited = [d["time"][day][0].split(":"), d["time"][day][1].split(":")];
				var val = (parseInt(splited[1][0]) + (parseInt(splited[1][1]) / 60))
				if (val > end) {
					end = val;
				}
				val = val - (parseInt(splited[0][0]) + (parseInt(splited[0][1]) / 60))
				return (val / 24 * 100) + "%";
			})
		d3.select("#gallerylist ul")
			.append("li")
			.attr("class", "curtime")
			.append("div")
			.attr("class", "time-bar")
			.append("div")
			.attr("class", "goodTimes")
			.style("left", ((start / 24 * 100) + "%"))
			.style("width", (((end - start) / 24 * 100) + "%"))
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
		this.settings.curDay = tempDate.getDay();
	};

	return out
}
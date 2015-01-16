var app = {
	settings: {

	},
	init: function() {
		app.galleryList.init();
	},
	loadMap: function() {

	}
}


app.galleryList = {
	SETTINGS: {
		galleryOpen: 24,
		galleryClose: 0,
		day: [
			"sun",
			"mon",
			"tue",
			"wed",
			"thu",
			"fri",
			"sat"
		]
	},
	init: function() {
		if ($("#gallerylist").length <= 0) {
			alert("no gallery list to initialize");
			return "no gallery list to init"
		}
		$("#gallerylist .gallery").each(app.galleryList.galleryListItem.init);
	},

	galleryListItem: {
		init: function(count, element) {
			app.galleryList.galleryListItem.timeScale.setTimeScaleOffSet(element);
			app.galleryList.galleryListItem.distance.init(element);
		},

		timeScale: {
			setTimeScaleOffSet: function(element) {
				var dayData = $(element).data(),
					currentElement = $(element).find(".hours")[0],
					currentData = $(currentElement).data();
				var d = new Date(),
					h = d.getDay()

				if (dayData.opening) {
					currentElement.innerHTML = dayData.timestring;
				} else {
					dayString = app.galleryList.SETTINGS.day[h];
					currentElement.innerHTML = currentData[dayString + "string"];
				}

				var parent = $(element).find(".time")[0].appendChild(document.createElement("div"));
				var scale = 700, // with 700 we look at a 24 hour period...
					timeback = 6; // we are looking 6 hours into the past...
				parent.style.width = scale + "%";
				parent.style.left = "-" + ((h / 7 + (d.getHours() / 168) - (timeback / 168)) * scale) + "%"

				for (var a = 0; a < 7; ++a) {
					app.galleryList.galleryListItem.timeScale.renderTime(parent, a, currentData[app.galleryList.SETTINGS.day[a] + "s"], currentData[app.galleryList.SETTINGS.day[a] + "e"])
				}
			},
			renderTime: function(parent, day, time1, time2) {
				if (time1 == "n/a") {
					return false;
				}
				// 168 total number hours in a week
				var left = ((day * 24) + parseFloat(time1)) / 168 * 100;
				var width = (time2 - time1) / 168 * 100;
				var element = document.createElement("div");
				element.className = app.galleryList.SETTINGS.day[day];
				element.style.width = width + "%";
				element.style.left = left + "%";
				element.innerHTML = app.galleryList.SETTINGS.day[day];
				parent.appendChild(element);
			},
		},

		distance: {
			init: function(element) {
				var distance = $(element).find(".distance")[0];
				if (navigator.geolocation) {
					distance.innerHTML = "finding you";
					app.galleryList.galleryListItem.distance.requestGPSdata(distance);
				} else {
					distance.innerHTML = "can't find you";
				} //TODO get the user lat lon and do math to find difference.
			},
			requestGPSdata: function(distance) {
				var disObject = $(distance).data()
				var helper = function(position) {
					var logDif = Math.abs(disObject.log - position.coords.longitude) * 111.320 * Math.cos(disObject.lat),
						latDif = Math.abs(disObject.lat - position.coords.latitude) * 110.54,
						dis = Math.round(Math.sqrt(Math.pow(logDif, 2) + Math.pow(latDif, 2)) * 100) / 100;
					distance.innerHTML = dis + "km";
				}
				navigator.geolocation.getCurrentPosition(helper);
			}
		}


	}
}
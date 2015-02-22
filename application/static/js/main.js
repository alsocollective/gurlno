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
			app.galleryList.galleryLoad.init(element);
		},

		timeScale: {
			//TODO render the state of reception over the daily time.
			setTimeScaleOffSet: function(element) {
				var dayData = $(element).data(),
					currentElement = $(element).find(".hours")[0],
					currentData = $(currentElement).data();
				var d = new Date(),
					h = d.getDay();

				if (dayData.timestring) {
					currentElement.innerHTML = dayData.timestring;
				} else {
					dayString = app.galleryList.SETTINGS.day[h];
					currentElement.innerHTML = currentData[dayString + "string"];
				}

				var parent = $(element).find(".time")[0].appendChild(document.createElement("div"));
				var scale = 1400, // with 700 we look at a 24 hour period...
					timeback = 0; // we are looking 6 hours into the past...
				parent.style.width = scale + "%";
				parent.style.left = ((((h - 7.5) / 7) + d.getHours() / 168) * scale) + "%";
				//(((h - 1) / 7 + (d.getHours() / 168) - (timeback / 168)) * scale) + "%"

				for (var a = 0; a < 7; ++a) {
					if (dayData.timestring && dayData.dayofweek + 1 == a) {
						app.galleryList.galleryListItem.timeScale.renderTime(parent, a, dayData.times, dayData.timee, true)
					} else {
						app.galleryList.galleryListItem.timeScale.renderTime(parent, a, currentData[app.galleryList.SETTINGS.day[a] + "s"], currentData[app.galleryList.SETTINGS.day[a] + "e"])
					}
				}
			},
			renderTime: function(parent, day, time1, time2, opening, receptionday) {
				if (time1 == "n/a") {
					return false;
				}
				// we need to render the background receptionday...
				if (opening) {
					app.galleryList
						.galleryListItem
						.timeScale
						.renderTime(parent, day, 0, time2, false, true);
				}
				// 168 total number hours in a week
				var right = ((day * 24) - (24 - parseFloat(time1))) / 168 * 100
				var width = (time2 - time1) / 168 * 100;
				var element = document.createElement("div");
				if (opening) {
					element.className = app.galleryList.SETTINGS.day[day] + " reception";
				} else if (receptionday) {
					element.className = app.galleryList.SETTINGS.day[day] + " receptionday";
				} else {
					element.className = app.galleryList.SETTINGS.day[day];
				}
				element.style.width = width + "%";
				element.style.right = right + "%";
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
	},
	galleryLoad: {
		// This is the swipping action to initialize the loading of the gallery
		// we use event's of swipe to trigger
		galleryContainer: false,
		init: function(element) {
			$(element).hammer().bind("panleft panright panstart panend", app.galleryList.galleryLoad.swipe)
		},
		swipe: function(ev) {
			if (app.galleryList.galleryLoad.galleryContainer == false) {
				app.galleryList.galleryLoad.galleryContainer = $("#gallerycontainer")[0];
			}
			if(ev.type == "panstart"){
				// $(app.galleryList.galleryLoad.galleryContainer).addClass("grabed")
			}
			if (ev.gesture.isFinal) {
				// TODO might want to change the trigger to momentum rather than width...
				// $(app.galleryList.galleryLoad.galleryContainer).removeClass("grabed")
				if (ev.gesture.deltaX < ev.currentTarget.clientWidth / -4 && !$(ev.currentTarget).hasClass("noshow")) {
					console.log(ev.currentTarget)
					app.gallery.loading.init(ev.currentTarget);
				} else {
					ev.currentTarget.style.left = 0;
					app.galleryList.galleryLoad.galleryContainer.style.left = 100 + "%";
				}
			} else if (ev.type == "panright" || ev.type == "panleft") {
				ev.currentTarget.style.left = ev.gesture.deltaX + "px";
				app.galleryList.galleryLoad.galleryContainer.style.left = ev.currentTarget.clientWidth + ev.gesture.deltaX + "px";
			}
		}
	}
}

app.gallery = {
	isLoading: false,
	init: function() {
		$("#gallerycontainer").addClass("nobackground");
		app.gallery.exit.init();
		app.gallery.initializeTimes();
	},
	// is what sets up and triggers the swipe away of the gallery
	exit: {
		init: function() {
			$('#gallerycontainer .gallerywrapper').hammer().bind("panleft panright panstart panend", app.gallery.exit.event)
		},
		element: false,
		event: function(ev) {
			//if it's a final event we check if we need to exit the gallery
			if (app.gallery.exit.exiting) {
				return false;
			}
			if (ev.type == "panend" /* ev.gesture.isFinal*/ ) {
				ev.currentTarget.style.left = 0;
				// when the gallery is more than half way past the center
				// this could be changed to if there was enough momentum or something along those lines...
				if (ev.gesture.deltaX > (ev.currentTarget.clientWidth / 4)) {
					// we reset all the perameters
					ev.currentTarget.parentNode.className = "";
					ev.currentTarget.parentNode.style.left = "";
					ev.currentTarget.parentNode.removeChild(ev.currentTarget);
				}
			} else if ((ev.type == "panright" || ev.type == "panleft") && ev.gesture.deltaX >= 0) {
				ev.currentTarget.style.left = ev.gesture.deltaX + "px";
			}
		},
		startToRemove: function() {
			var el = $("#gallerycontainer .gallerywrapper")[0]
		}
	},

	loading: {
		init: function(target) {
			var gallerycontainer = $("#gallerycontainer");

			//prevent multiple triggerings of the loading event
			if (app.gallery.loading == true || gallerycontainer.hasClass(target.id)) {
				return false;
			}

			//clear everything
			app.gallery.isLoading = true;
			gallerycontainer[0].innerHTML = "";

			//move the slider and container to the far left
			gallerycontainer.addClass("show");
			gallerycontainer[0].style.left = "0px";

			// setup to prevent double loading of the same page...
			gallerycontainer.addClass(target.id);
			gallerycontainer.load("/currentshow/" + target.id, app.gallery.loading.sucess);

			// reset the slider to it's 0 position
			target.style.left = 0;
		},
		sucess: function(var1, var2) {
			app.gallery.isLoading = false;
			app.gallery.init();
		},
		fail: function() {

		}
	},
	initializeTimes: function() {
		// get the varablese
		var parent = $(".gallerywrapper"),
			galleryid = parent.data().id,
			galleryData = parent.find(".hours").data(),
			day = app.galleryList.SETTINGS.day[new Date().getDay()];

		// set the gallery opening time for the day
		$(parent).find(".hours").html(galleryData[day + "string"])
		// set distacne
		$(parent).find(".distance").html($("#" + galleryid).find(".distance").html())
	}
}
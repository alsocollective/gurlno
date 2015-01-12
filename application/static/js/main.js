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
		galleryClose: 0
	},
	init: function() {
		if ($("#gallerylist").length <= 0) {
			alert("no gallery list to initialize");
			return "no gallery list to init"
		}
		app.galleryList.findMinMaxTimeOfOperations();
		$("#gallerylist .gallery").each(app.galleryList.galleryListItem.init);
	},

	findMinMaxTimeOfOperations: function() {
		$("#gallerylist .hours").each(app.galleryList.findMinMaxTimeOfOperationsHelper);
		app.galleryList.SETTINGS.galleryTotalOpenTime = app.galleryList.SETTINGS.galleryClose - app.galleryList.SETTINGS.galleryOpen;
	},
	findMinMaxTimeOfOperationsHelper: function(counter, element) {
		var currentData = $(element).data();
		currentData.start = parseFloat(currentData.start);
		currentData.end = parseFloat(currentData.end);
		if (app.galleryList.SETTINGS.galleryOpen > currentData.start) {
			app.galleryList.SETTINGS.galleryOpen = currentData.start;
		}
		if (app.galleryList.SETTINGS.galleryClose < currentData.end) {
			app.galleryList.SETTINGS.galleryClose = currentData.end;
		}
	},

	galleryListItem: {
		init: function(count, element) {
			console.log(element);
			app.galleryList.galleryListItem.setTimeScaleOffSet(element);
			app.galleryList.galleryListItem.setDistance(element);
		},
		setTimeScaleOffSet: function(element) {
			var currentData = $($(element).find(".hours")[0]).data();
			currentData.start = parseFloat(currentData.start);
			currentData.end = parseFloat(currentData.end);
			var movingElement = $($(element).find(".time")[0]);
			var width = (currentData.end - currentData.start) / app.galleryList.SETTINGS.galleryTotalOpenTime * 100;
			var left = (currentData.start - app.galleryList.SETTINGS.galleryOpen) / app.galleryList.SETTINGS.galleryTotalOpenTime * 100; //(currentData.start - app.galleryList.SETTINGS.galleryTotalOpenTime) / app.galleryList.SETTINGS.galleryTotalOpenTime * 100;
			movingElement.width(width + "%");
			movingElement[0].style.left = left + "%";

		},
		setDistance: function(element) {
			var distance = $(element).find(".distance")[0];
			distance.innerHTML = $(distance).data();
			//TODO get the user lat lon and do math to find difference.
		}
	}
}
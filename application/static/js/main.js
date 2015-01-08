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
		},
		setTimeScaleOffSet: function(element) {
			var currentData = $($(element).find(".hours")[0]).data();
			currentData.start = parseFloat(currentData.start);
			currentData.end = parseFloat(currentData.end);
			var movingElement = $($(element).find(".time")[0]);
			var width = (currentData.end - currentData.start) / app.galleryList.SETTINGS.galleryTotalOpenTime * 100;
			//TODO off set left!!!
			movingElement.width(width + "%");

		},
		setDistance: function(element) {
			//TODO get the user lat lon and do math to find difference.
		}
	}
}
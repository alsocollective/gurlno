from django.contrib import admin
from galleries.models import *
# Register your models here.



class gal_inline_date(admin.StackedInline):
	model = HoursOfOp
	extra = 1
	fieldsets = [
		('',{
				'fields':[("mon_start","mon_end"),("tue_start","tue_end"),("wed_start","wed_end"),("thu_start","thu_end"),("fri_start","fri_end"),("sat_start","sat_end"),("sun_start","sun_end")]
		}),
	]

class gal_admin(admin.ModelAdmin):
	fieldsets = [
		('',{
			'fields':[
				("title","logo"),
				("description","gallorist","gallery_tyle"),
				("url","facebook","instagram","twitter",),
				("address","log","lat","neighbourhood","google_place_key"),
				("phone","email",),
				("mon_start","mon_end"),
				("tue_start","tue_end"),
				("wed_start","wed_end"),
				("thu_start","thu_end"),
				("fri_start","fri_end"),
				("sat_start","sat_end"),
				("sun_start","sun_end"),
				("timeDateAsString","easyReadDate"),
				("slug","next_show"),
			]}
		),]	
	inlines = [gal_inline_date,]

class show_admin(admin.ModelAdmin):
	fieldsets = [
		('main',{
			'fields':[
				("title","gallery"),
				("opening_start","opening_start_time"),("opening_end","opening_end_time"),				
				("date_start","date_start_time"),("date_end","date_end_time"),
				("description","description_author","description_link"),
				"includes_artists",
				"tags",
				("cover_work","includes_works"),
				("link","facebook")
			]},),
		('secondary',{
			'classes': ('collapse',),
			'fields':[
				"days_showing",
				"currator",
				"arttype",
				"cover"

			]}),
		]
	filter_horizontal = ('includes_artists',)

class artist_admin(admin.ModelAdmin):
	fieldsets = [
		("main",{
			'fields':[
				("first_name","last_name",),
				"bio",
				"website",
				("facebook","instagram","twitter","tublr",),
				("email","phone",)
			]}),
	]

class image_admin(admin.ModelAdmin):
	fieldsets = [
		("main",{
			'fields':[
				("title","alttext"),
				"Image",
				"creator",
				("description","medium"),
			]}),
	]
	pass

	
admin.site.register(Gallery,gal_admin)
admin.site.register(artType)
admin.site.register(Show,show_admin)
admin.site.register(WorkMedium)
admin.site.register(Artist,artist_admin)
admin.site.register(WorkImage,image_admin)
admin.site.register(Neighbourhood)
admin.site.register(HoursOfOp)
admin.site.register(Day)
admin.site.register(Tag)
admin.site.register(Gallorist)
admin.site.register(Gallery_Type)
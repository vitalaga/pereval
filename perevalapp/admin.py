from django.contrib import admin
from .models import Users, PerevalAdded, Coords, Images, Level


class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'fam', 'otc', 'phone')


class CoordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'height')


class LevelAdmin(admin.ModelAdmin):
    ist_display = ('id', 'winter', 'summer', 'autumn', 'spring')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'pereval', 'title')


class PerevalAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'coords', 'level', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'status',
    )


admin.site.register(PerevalAdded, PerevalAdmin)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Users, UsersAdmin)

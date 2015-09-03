from django.contrib import admin
from .models import *

class ArtistAdmin(admin.ModelAdmin):
    pass

class FestivalAdmin(admin.ModelAdmin):
    pass


class RankingSetAdmin(admin.ModelAdmin):
    pass


class RankingAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass



admin.site.register(Artist, ArtistAdmin)
admin.site.register(Festival, FestivalAdmin)
admin.site.register(Ranking, RankingAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(RankingSet, RankingSetAdmin)
from django.contrib import admin
from mainapp.models import(
    Teacher,School,Galeria,News,Rewiew
)

# Register your models here.


admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Galeria)
admin.site.register(Rewiew)
admin.site.register(News)

from django.contrib import admin

from .models import Flight, Airport,Passenger

# Register your models here.

# necesario para dibujar esto al iniciar sesion en admin del proyecto
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):

    filter_horizontal = ("flight",)

admin.site.register(Airport)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger,PassengerAdmin)


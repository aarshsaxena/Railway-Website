from django.contrib import admin
from bookings.models import Tickets

class TicketsAdmin(admin.ModelAdmin):
    list_display=('pnr','transactionid','email','trainno','trainname','source','destination','kms','classs','doj','amt','passno','list1')
admin.site.register(Tickets,TicketsAdmin)
# Register your models here.
# Aarsh Saxena (21bec001)

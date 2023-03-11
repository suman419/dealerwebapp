from django.contrib import admin
from django.forms import models
from.models import Anumandal, Block, Panchayat, Dealer

# Register your models here.
@admin.register(Anumandal)
class AnumandalModelAdmin(admin.ModelAdmin):
    list_display =['id','name','created_at']

@admin.register(Block)
class BlockModelAdmin(admin.ModelAdmin):
    list_display =['id','name','created_at']

@admin.register(Panchayat)
class PanchayatModelAdmin(admin.ModelAdmin):
    list_display =['id','name','created_at']

@admin.register(Dealer)
class DealeraddModelAdmin(admin.ModelAdmin):
    list_display =['id','full_name','mobile_number','email','aadhar_number','created_at']

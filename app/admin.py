from django.contrib import admin

# Register your models here.
from .models import Bolimlar,Hodimlar, Hodim_haqida, Qarindoshlik


class HodimAdmin(admin.ModelAdmin):
    list_display = ['ism_sharifi','bolimi','lavozimi','stavka']
    list_per_page = 10
    search_fields = ['ism_sharifi']
    class Meta:
        model = Hodim_haqida
admin.site.register(Hodimlar, HodimAdmin)


class BolimAdmin(admin.ModelAdmin):
    list_display = ['nomi']
    list_per_page = 10
    search_fields = ['nomi']
admin.site.register(Bolimlar, BolimAdmin)

class QarindoshInline(admin.TabularInline):
    model = Qarindoshlik
    fields = ["qarindoshligi","qarindosh_ismi","qarindosh_tug_yil",'yashash_joyi','ish_joyi']
@admin.register(Hodim_haqida)

class Hodim_haqidaAdmin(admin.ModelAdmin):
    inlines = [QarindoshInline, ]
    # search_fields = ['ism_sharifi']
    list_per_page = 10
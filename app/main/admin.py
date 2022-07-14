from django.contrib import admin

from main.models import Email, Food, FoodsPictures
from django.utils.html import format_html

class FoodsPicturesInline(admin.TabularInline):
    model = FoodsPictures
    readonly_fields = ["thumbnail", "imgsize"]

    def thumbnail(self,instance):
        if instance.picture.name != "":
            return format_html(f"<img src='{instance.picture.url}' class='thumbnail'/>")
        return ''
    def imgsize(self,instance):
        if instance.picture.name != "":
            return f"{int(instance.picture.size / 1024)} KB"
        return ""



@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    inlines = [FoodsPicturesInline,]

    class Media:
        css = {
            "all": ["styles.css"]
        }

@admin.register(FoodsPictures)
class FoodsPicturesAdmin(admin.ModelAdmin):
    list_display = ["food" ,"picture",]

@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass
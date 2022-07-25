from django.contrib import admin

from main.models import Email, Shop, ShopPictures
from django.utils.html import format_html

class ShopsPicturesInline(admin.TabularInline):
    model = ShopPictures
    readonly_fields = ["thumbnail", "imgsize"]

    def thumbnail(self,instance):
        if instance.picture.name != "":
            return format_html(f"<img src='{instance.picture.url}' class='thumbnail'/>")
        return ''
    def imgsize(self,instance):
        if instance.picture.name != "":
            return f"{int(instance.picture.size / 1024)} KB"
        return ""



@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [ShopsPicturesInline,]

    class Media:
        css = {
            "all": ["styles.css"]
        }


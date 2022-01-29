from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CmsSlider


# Register your models here.

class CmsAdmin(admin.ModelAdmin):
    list_display = ('cms_title', 'cms_text', 'cms_css', 'get_Img')
    list_display_links = ('cms_title',)
    list_editable = ('cms_css',)
    fields = ('cms_title', 'cms_text', 'cms_css', 'get_Img')
    readonly_fields = ('get_Img',)

    def get_Img(self, img):
        if img.cms_img:
            return mark_safe(f'<img src ="{img.cms_img.url}" width="80px"')
        else:
            return 'нету картинки'

    get_Img.short_description = 'картинки'


admin.site.register(CmsSlider, CmsAdmin)

from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm


# Register your models here.

class Coment(admin.StackedInline):
    model = ComentCrm  # обязательный атрибут показывающий к какой моделе класс отностится
    fields = ('covent_data', 'coment_text',)
    readonly_fields = ('covent_data', )
    extra = 0 # кол-во полей для ввода комитов


class AdminOrder(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone')
    list_display_links = ('id', 'order_name')  # сделаем кликабельным имя
    search_fields = ('id', 'order_status', 'order_name', 'order_phone')  # добавим виджет поиска
    list_filter = ('order_status',)  # фильтр, никогда не будет лишним
    list_editable = ('order_status',
                     'order_phone')  # а тут сделаем поля с возможностью редактирования, не будем тратить время на провал в карточку.
    list_per_page = 10  # пагинация, стало удобнее,как добавил.
    list_max_show_all = 50
    fields = ('id', 'order_status', 'order_data', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_data',)
    # передаем класс в поле класса Order
    inlines = [Coment, ]


admin.site.register(StatusCrm)
admin.site.register(Order, AdminOrder)
admin.site.register(ComentCrm)

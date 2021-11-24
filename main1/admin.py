from django.contrib import admin
from .models import GoodsType, GoodsCategory, Good, Cart, gComment

class GoodInline(admin.TabularInline):                             ## новый класс, чтобы отобразить товары внутри
    model = Good

class СatsInline(admin.TabularInline):                             ## новый класс, чтобы отобразить категории внутри
    model = GoodsCategory

class CommentsInline(admin.TabularInline):                             ## новый класс, чтобы отобразить комментарии внутри
    model = gComment

class GoodsTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'addr', 'imageLink')
    inlines = [СatsInline]
admin.site.register(GoodsType, GoodsTypeAdmin)

class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'addr', 'linkT')
    inlines = [GoodInline]
admin.site.register(GoodsCategory, GoodsCategoryAdmin)

class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'linkC', 'dateAdded', 'imageLink', 'price' )
    list_filter = ('linkT', 'linkC', 'dateAdded', 'imageLink', 'price')     ## фильтры
    fieldsets = (                                                           ## группировки
        ('Main', {
            'fields': ('name','price')
        }),
        ('Groups', {
            'fields': ('linkT','linkC')
        }),        
        ('Propertyes', {
            'fields': ('dateAdded', 'imageLink')
        }),
    )
    inlines = [CommentsInline]
admin.site.register(Good,GoodAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ('linkU', 'linkG', 'price')
    list_filter  = ('linkU', 'linkG')
admin.site.register(Cart, CartAdmin)
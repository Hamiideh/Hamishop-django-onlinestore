from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Product, Comment, Category


class ProductCommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars' ,'active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active', 'inventory', 'inventory_status', 'category' ]
    list_editable = ['price']
    ordering = ['-datetime_created']
    list_filter = ['datetime_created', 'category']
    list_select_related = ['category']
    search_fields = ['title__istartswith', 'inventory__istartswith' ]

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        if product.inventory > 50:
            return 'High'
        return 'Medium'

    @admin.display(ordering='category__title', description='category')
    def product_category(self, product):
        return product.category.title



    inlines = [ProductCommentInline,]


@admin.register(Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars' ,'active',]
    autocomplete_fields = ['product',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin

from server.models import Ingredient, Pizza, PizzaOrder

@admin.register(PizzaOrder)
class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'status', 'user_id')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'user')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'status')
        }),
        ('Pizzas', {
            'fields': ('pizzas',)
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        })
    )
    filter_horizontal = ('pizzas',)
    list_per_page = 25
    list_max_show_all = 25
    list_editable = ('status',)
    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        queryset.update(status='paid')
    mark_as_paid.short_description = "Mark selected orders as paid"
    mark_as_paid.allowed_permissions = ('change',)

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
        ('Ingredients', {
            'fields': ('ingredients',)
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        })
    )
    filter_horizontal = ('ingredients',)
    list_per_page = 25
    list_max_show_all = 25
    list_editable = ('price',)

@admin.register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
        ('Timestamps', {
            'classes': ('collapse',),
            'fields': ('created_at', 'updated_at')
        })
    )
    list_per_page = 25
    list_max_show_all = 25
    list_editable = ('price',)
    

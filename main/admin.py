from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active", "is_home",'slug','selected_categories',)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    search_help_text = (" You can search the blogs by title and description")
    readonly_fields = ("slug",)
    list_filter = ("categories","is_active", "is_home",)

    def selected_categories(self,obj):
        html = "<ul>"
        for category in obj.categories.all():
            html += "<li>" + category.name + "</li>"
        
        html += "</ul>"
        return mark_safe(html)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
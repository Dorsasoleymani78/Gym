from django.contrib import admin

# Register your models here.
from .models import Blog 
from django.utils.html import format_html
 
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('photo_tag',)
    list_display=('title','les_content','photo_tag','is_active','click_me')
    list_filter=('is_active','create_at')
    search_fields=['category']
    list_per_page=2
    
    def les_content(self,obj):
        return obj.content[:100]
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/Blog/blog/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    
    def photo_tag(self,obj):
        return format_html(f'<img  src="/media/{obj.img}" style=height:100px;width:100px>')
    
    click_me.short_description=' ویرایش '
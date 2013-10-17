from django.contrib import admin
from blogs.models import Post , Image


class CommentInline(admin.TabularInline):
    model = Image
    extra = 3
    
    
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['post_title', 'post_text']}),
        ('Date information' ,   {'fields': ['pub_date'] , 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('post_title' , 'pub_date' , 'is_active')
    list_filter = ['pub_date']
    search_fields = ['blog_title']
    date_hierarchy = 'pub_date'
    
admin.site.register(Post, BlogAdmin)



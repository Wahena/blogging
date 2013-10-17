from django.contrib import admin
from blogs.models import Blog , Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3
    
    
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['blog_text']}),
        ('Date information' ,   {'fields': ['pub_date'] , 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('blog_text' , 'pub_date' , 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['blog_text']
    date_hierarchy = 'pub_date'
    
admin.site.register(Blog, BlogAdmin)



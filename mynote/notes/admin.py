from django.contrib import admin
from notes.models import Post, Comment

class ChoiceInline(admin.StackedInline):
    model = Comment
    extra = 0
    fieldsets = [
        # Uncomment this line to enable editing the comment
        #(None, {'fields': ['comment_text']}),
        ('Publish info', {'fields': ['commented_date'], 'classes': ['collapse']}),
    ]

class PostAdmin(admin.ModelAdmin):
    #fields = ['publisheddate', 'posttext']

    list_display = ('post_text', 'published_date')
    list_filter = ['published_date']
    search_fields = ['post_text']

    fieldsets = [
        (None, {'fields': ['post_text']}),
        ('Publish info', {'fields': ['published_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Post, PostAdmin)
#admin.site.register(Comment)
from django.contrib import admin
from blogging.models import Post, Category



# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    # stop from being able to link to posts from the category admin page
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
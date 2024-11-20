from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    # stop from being able to link to posts from the category admin page
    exclude = ('posts',)

# function to allow the admin to add categories to posts
class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 1

# class to allow the admin to add categories to posts
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

# register the models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
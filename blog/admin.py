from django.contrib import admin
from .models import Post, Category, Tag, Produce, OptionColors,Comment
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)} # 카테고리 모델의 name 필드에 값이 입력될 때
    # 자동으로 slug가 만들어진다.


admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)

class ProduceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Produce,ProduceAdmin)

class OptionColorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(OptionColors,OptionColorsAdmin)

admin.site.register(Comment)
# Register your models here.

from django.contrib import admin
from catalog.models import Author,Genre,Book,BookInstance,Language
# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name','first_name','date_of_birth','date_of_death')

admin.site.register(Author,AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author')
    inlines=[BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book','due_back')
    list_filter=('status','due_back')

    fieldsets=(
    (None,{'fields':('book','imprint','id')}),
    ('availability',{'fields':('status','due_back')}),
    )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

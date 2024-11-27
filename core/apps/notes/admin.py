from django.contrib import admin


from core.apps.notes.models import Note, NoteList

# Register your models here.


@admin.register(NoteList)
class NoteListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'customer', 'created_at')
    filter_horizontal = ('notes',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'customer', 'is_checked',
                    'is_important', 'created_at')

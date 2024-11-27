from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.models import Customer

from core.apps.notes.entities import Note as NoteEntity

# Create your models here.


class Note(TimedBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name='Покупатель',
        on_delete=models.CASCADE,
        related_name='notes',
    )
    is_checked = models.BooleanField(
        verbose_name='Отмечено ли',
        default=False,
    )
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=255,
    )
    text = models.TextField(
        verbose_name='Текст заметки',
        blank=True,
    )
    is_important = models.BooleanField(
        verbose_name='Важно ли',
        default=False,
    )

    def to_entity(self) -> NoteEntity:
        return NoteEntity(
            id=self.id,
            customer_id=self.customer.pk,
            is_checked=self.is_checked,
            title=self.title,
            text=self.text,
            is_important=self.is_important,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class NoteList(TimedBaseModel):
    customer = models.ForeignKey(
        Customer,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='note_list',
    )
    name = models.CharField(
        verbose_name='Название списка',
        max_length=255,
        unique=True,
    )
    notes = models.ManyToManyField(
        'Note',
        verbose_name='Заметки',
    )

    class Meta:
        verbose_name = 'Список заметок'
        verbose_name_plural = 'Списки заметок'

    def __str__(self) -> str:
        return self.name

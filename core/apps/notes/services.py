from core.apps.customers.entities import CustomerEntity
from core.apps.customers.models import Customer
from core.apps.notes.models import Note, NoteList


class ORMNotesService:
    def get_list_notes(self, customer_entity: CustomerEntity):
        note_list = Customer.from_entity(customer_entity).note_list
        res = {}
        for note_list_obj in note_list.all():
            res[note_list_obj.name] = [note.to_entity()
                                       for note in note_list_obj.notes.all()]
            res[note_list_obj.name].sort(key=lambda x: x.id)
            # res[note_list_obj.name] = []
            # for ind, note in enumerate(note_list_obj.notes.all(), 1):
            #     note_entity = note.to_entity()
            #     note = {
            #         'id': note_entity.id,
            #         'note_id': ind,
            #         'customer_id': note_entity.customer_id,
            #         'title': note_entity.title,
            #         'text': note_entity.text,
            #         'is_important': note_entity.is_important,
            #         'is_checked': note_entity.is_checked,
            #         'created_at': note_entity.created_at,
            #         'updated_at': note_entity.updated_at,
            #     }
            #     res[note_list_obj.name].append(note)
        return res

    def create_note_list(self, customer_entity: CustomerEntity, name: str):
        NoteList.objects.create(
            name=name,
            customer=Customer.from_entity(customer_entity),
        )
        return customer_entity.id

    def add_note_to_list(self,
                         customer_entity: CustomerEntity,
                         list_name: str,
                         title: str,
                         note_text: str,
                         is_important: bool,
                         ):
        note_list = NoteList.objects.get(
            customer=Customer.from_entity(customer_entity),
            name=list_name,
        )
        note = Note.objects.create(
            customer=Customer.from_entity(customer_entity),
            title=title,
            text=note_text,
            is_important=is_important,
        )
        note_list.notes.add(note)
        return note.to_entity()

    def change_checkbox(self,
                        customer_entity: CustomerEntity,
                        note_id: int,
                        ):
        customer = Customer.from_entity(customer_entity)
        note = Note.objects.get(customer=customer, id=note_id)
        note.is_checked = not note.is_checked
        note.save()
        return note.to_entity()

from dataclasses import dataclass

from core.apps.customers.services.customers import ORMCustomerService
from core.apps.notes.services import ORMNotesService


@dataclass
class GetNotesListUseCase:
    customer_service: ORMCustomerService
    notes_service: ORMNotesService

    def execute(self, customer_token: str):
        customer = self.customer_service.get_by_token(customer_token)
        notes = self.notes_service.get_list_notes(customer)
        return notes


@dataclass
class CreateListUseCase:
    customer_service: ORMCustomerService
    notes_service: ORMNotesService

    def execute(
            self,
            customer_token: str,
            name: str,
    ):
        customer = self.customer_service.get_by_token(customer_token)
        customer_id = self.notes_service.create_note_list(customer, name)
        return customer_id


@dataclass
class AddNoteToListUseCase:
    customer_service: ORMCustomerService
    notes_service: ORMNotesService

    def execute(
            self,
            customer_token: str,
            list_name: int,
            title: str,
            text: str,
            is_important: bool,
    ):
        customer = self.customer_service.get_by_token(customer_token)
        note = self.notes_service.add_note_to_list(
            customer,
            list_name,
            title,
            text,
            is_important,
        )

        return note


@dataclass
class ChangeCheckboxUseCase:
    customer_service: ORMCustomerService
    notes_service: ORMNotesService

    def execute(
            self,
            customer_token: str,
            note_id: int,
    ):
        customer = self.customer_service.get_by_token(customer_token)
        note = self.notes_service.change_checkbox(customer, note_id)
        return note

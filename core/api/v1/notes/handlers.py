from core.api.filters import PaginationIn
from core.api.schemas import ApiResponse, ListPaginatedResponse, ListResponse
from core.api.v1.notes.schemas import AddNoteToListSchemaIn, CreateListSchemaIn
from core.apps.customers.services.customers import ORMCustomerService
from core.apps.notes.services import ORMNotesService
from django.http import HttpRequest
from ninja import Router, Header

from core.apps.notes.use_cases import AddNoteToListUseCase, ChangeCheckboxUseCase, CreateListUseCase, GetNotesListUseCase

router = Router(tags=['Notes'])


@router.get('', response=ApiResponse)
def get_all_lists_handler(
        request: HttpRequest,
        token: str = Header(alias='Auth-Token'),
) -> ApiResponse:

    use_case = GetNotesListUseCase(
        ORMCustomerService(),
        ORMNotesService(),
    )
    items = use_case.execute(customer_token=token)

    return ApiResponse(data=items)


@router.post('/create_list', response=ApiResponse)
def create_list_handler(
    request: HttpRequest,
    schema: CreateListSchemaIn,
    token: str = Header(alias='Auth-Token'),
):
    use_case = CreateListUseCase(
        ORMCustomerService(),
        ORMNotesService(),
    )
    customer_id = use_case.execute(customer_token=token, name=schema.name)
    return ApiResponse(data=customer_id)


@router.post('/{list_name}/add_note', response=ApiResponse)
def add_note_to_list_handler(
    request: HttpRequest,
    list_name: str,
    schema: AddNoteToListSchemaIn,
    token: str = Header(alias='Auth-Token'),
):
    use_case = AddNoteToListUseCase(
        ORMCustomerService(),
        ORMNotesService(),
    )
    note = use_case.execute(
        customer_token=token,
        title=schema.title,
        text=schema.text,
        is_important=schema.is_important,
        list_name=list_name,
    )
    return ApiResponse(data=note)


@router.post('/check/{note_id}', response=ApiResponse)
def change_checkbox(
        request: HttpRequest,
        note_id: int,
        token: str = Header(alias='Auth-Token'),
):
    use_case = ChangeCheckboxUseCase(
        ORMCustomerService(),
        ORMNotesService(),
    )
    note = use_case.execute(
        customer_token=token,
        note_id=note_id,
    )
    return ApiResponse(data=note)

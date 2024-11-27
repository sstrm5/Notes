from ninja import Schema


class CreateListSchemaIn(Schema):
    name: str | None = None


class AddNoteToListSchemaIn(Schema):
    title: str
    text: str | None = None
    is_important: bool | None = None

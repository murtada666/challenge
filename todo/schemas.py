from ninja import Schema



class note_schema(Schema):
    id: int
    titel: str
    description: str
    
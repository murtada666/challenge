from typing import List
from ninja import Router
from todo.models import note
from todo.schemas import note_schema


todo_router = Router(tags=["todo"])



@todo_router.get("get_all_notes", response=List[note_schema])
def get_note(request):
    result = note.objects.all()
    
    return result


@todo_router.get("get_note", response=note_schema)
def get_note(request, note_id: int):
    result = note.objects.get(id = note_id)
    
    return result


@todo_router.post("make_note", response=note_schema)
def make_note(request, note_id: int, note_titel: str, note_description: str):
    new_note = note.objects.create(
        id = note_id,
        titel = note_titel,
        description = note_description
        )
    
    return new_note




@todo_router.put("update_note")
def update_note(request, note_titel:str, updated_description:str):
    
    note.objects.filter(
        titel = note_titel
        ).update(description = updated_description)
    
    return {"message": "updated"}
    



@todo_router.delete("del_note")
def del_note(request, note_id: int):
    note.objects.filter(id = note_id).delete()
    
    return {"message": "Deleted"}
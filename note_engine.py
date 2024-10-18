from llama_index.core.tools import FunctionTool
import os

note_path = 'notes/note.txt'

def save_note(note):
    if not os.path.exists(note_path):
        open(note_path, "w")
    with open(note_path, "a") as f:
        f.writelines([note + "\n"])
    return 'Saved note'


note_engine = FunctionTool.from_defaults(
    fn=save_note,
    name="note_saver",
    description="this tool can save a text based note to a file for the user",
)
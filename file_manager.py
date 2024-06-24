import json

# save notes to file
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file)
        

# load notes from file
def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

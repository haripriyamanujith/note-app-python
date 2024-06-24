from file_manager import save_notes, load_notes
from messages import create_note_msg, no_changers, all_notes

notes = load_notes()

# Create note
def create_note():
    title = input("Enter The Note Title: ")
    messege = input("Enter the Messege: ")
    if title and messege != "":
        notes[title] = messege
        save_notes(notes)
        print(create_note_msg)
    else:
        print(no_changers)

# display all notes
def show_all_notes():
    print(all_notes)
    for index, (key, value) in enumerate(notes.items(), start=1):
        print(f"{index}. --{key}-- \n   {value}\n")
    print("\n")

#edit selected note
def edit_note():
    while True:
        try:
            note_number = int(input("Enter The Note Number You Want To Edit: "))
            if 1 <= note_number <= len(notes):
                old_key = list(notes.keys())[note_number - 1]
                new_key = input(f"Enter The New Title For Note '{old_key}': ")
                if new_key == "":
                    new_key = old_key
                else:
                    notes[new_key] = notes.pop(old_key)
                old_value = notes[new_key]
                new_value = input(f"Enter The New Message For Note '{old_key}': ")

                if new_value == "":
                    notes[new_key] = old_value
                else:
                    notes[new_key] = new_value  # Update the value of the task
                save_notes(notes)  # Save the updated notes to file
                print(f"\n***************************************\n** Note '{old_key}' Updated Successfully **\n***************************************\n")    
            else:
                raise ValueError
        except ValueError:
            continue
        break

# delete selected note
def delete_note():
    while True:
        try:
            note_number = int(input("Which Note Do You Want To Delete: "))
            if 1 <= note_number <= len(notes):
                notes_keys = list(notes.keys())[note_number - 1]  # Get the note key corresponding to the index
                del notes[notes_keys]  # Delete the note
                save_notes(notes)  # Save the updated notes to file
                print(f"\n***************************************\n** Note '{notes_keys}' Deleted Successfully **\n***************************************\n")
            else:
                raise ValueError
        except ValueError:
            continue
        break
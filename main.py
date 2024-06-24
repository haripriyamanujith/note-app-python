from file_manager import load_notes
from note_manager import create_note, show_all_notes, edit_note, delete_note
from messages import title, menu, exit, value_error_msg




notes = load_notes()

def main():
    print(title)

    
    while True:
        try:
            print(menu)
            user_input = int(input("Enter Your option: "))
            print("\n")
            if  5 >= user_input >= 1:
                if user_input == 1:
                    create_note() 
                elif user_input == 2:
                    show_all_notes()
                elif user_input == 3:
                    show_all_notes()
                    edit_note()
                elif user_input == 4:
                    show_all_notes()
                    delete_note()
                elif user_input == 5:
                    print(exit)
                    break
                
                    
            else:
                raise ValueError
        except ValueError:
            print(value_error_msg)
            continue
        except KeyboardInterrupt:
            print(exit)
            break



if __name__ == "__main__":
    main()

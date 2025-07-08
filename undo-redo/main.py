undo_stack = []
redo_stack = []

text = ""

def show_menu():
    print("\nOptions")
    print("1. Type new text")
    print("2. Undo")
    print("3. Redo")
    print("4. Show current text")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        new_text = input("Enter text to append: ")
        undo_stack.append(text)   # Save current text to undo stack
        text += new_text          # Append new text
        redo_stack.clear()        # Clear redo stack on new change

    elif choice == "2":
        if undo_stack:
            redo_stack.append(text)   # Save current text for redo
            text = undo_stack.pop()   # Undo
        else:
            print("Nothing to undo.")

    elif choice == "3":
        if redo_stack:
            undo_stack.append(text)   # Save current text for undo
            text = redo_stack.pop()   # Redo
        else:
            print("Nothing to redo.")

    elif choice == "4":
        print("\nCurrent Text:", text)

    elif choice == "5":
        print("Exiting editor...")
        break

    else:
        print("Invalid choice. Please choose number between 1 to 5.")

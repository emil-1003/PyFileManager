import os
from modules.functions import create_file, create_dir, delete_file, delete_empty_dir, delete_dir_with_content, rename, move_file, show_content

def clear_screen():
    os.system('cls')

def main():
    root = input("# Type root directory: ")
    
    while True:
        clear_screen()
        print("You are at", root)
        
        action = input(
            "# Type 1 to create new file\n"
            "# Type 2 to create new dir\n"
            "# Type 3 to remove file\n"
            "# Type 4 to remove empty dir\n"
            "# Type 5 to remove dir with its content\n"
            "# Type 6 to rename a file/dir\n"
            "# Type 7 to move file\n"
            "# Type 8 to change root path\n"
            "# Type 9 to view content\n"
            "# Type 'exit' to exit\nYour input: "
        )
        clear_screen()
        
        print("You are at", root)
        
        actions = {
            "1": create_file,
            "2": create_dir,
            "3": delete_file,
            "4": delete_empty_dir,
            "5": delete_dir_with_content,
            "6": rename,
            "7": move_file,
            "8": lambda: input("# Type new root directory: "),
            "9": show_content,
            "exit": lambda: exit()
        }
        
        try:
            if action in actions:
                if action == "8":
                    root = actions[action]()
                else:
                    actions[action](root)
            else:
                print("Wrong input!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
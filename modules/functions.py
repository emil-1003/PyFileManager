import os
import shutil

def create_file(root):
    file_name = input("# Type new file name: ")
    f = open(root+file_name, "a")
    content = input("# Write to file: ")
    f.write(content)
    f.close()
    
def create_dir(root):
    dir_name = input("# Type new dir name: ")
    os.mkdir(root+dir_name)
    
def delete_file(root):
    file_name = input("# Type file name to delete: ")
    os.remove(root+file_name)
    
def delete_empty_dir(root):
    dir_name = input("# Type name of empty dir to delete: ")
    os.rmdir(root+dir_name)
    
def delete_dir_with_content(root):
    print("At the moment it does not work with nested directories!")
    dir_name = input("# Type dir name to delete with all its content: ")
    for root, dirs, files in os.walk(root+dir_name):
        for file in files:
            print("prøver og slette: "+root+file)
            os.remove(root+"/"+file)
    os.rmdir(root)
    
def rename(root):
    old_name = input("# Type file/dir to rename: ")
    new_name = input("# Type new name: ")
    os.rename(old_name, new_name)
    
def move_file(root):
    file_to_move = input("# Type file to move: ")
    dst_path = input("# Type destination to move file: ")
    shutil.move(root+file_to_move, dst_path+file_to_move)
            
def show_content(root_path):
    for root, _, files in os.walk(root_path):
        # x = re.split(r'[\\/]', root)
        # print(x[-1]+"/")
        
        print(root)
        for f in files:
            print(root+"/"+f)
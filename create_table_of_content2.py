# Program for sidebar generation
# reference:  https://stackoverflow.com/questions/51216965/gitlab-custom-wiki-sidebar-not-working

import os
import glob
ignore_list = [".git", ".idea", "create_table_of_content2.py","_sidebar.md"]
spaces = "    "
c = os.getcwd()

def get_all_files_and_directories(path, depth):
    spaces_tmp = spaces*depth    
    file_list = os.listdir(path)    
    for f in file_list:
        if f in ignore_list:
            continue
        if os.path.isdir(path+"/"+f):
            writepath=(path+"/"+f)
            writepath=writepath.replace(c, '.')
            sidebar.write(f'{spaces_tmp}- [{f}]({writepath})'+ "\n")
            get_all_files_and_directories(path+"/"+f, depth+1)
        elif f.split(".")[-1] == "md":
            writepath=(path+"/"+f)
            writepath=writepath.replace(c, '.')
            sidebar.write(f'{spaces_tmp}- [{f.split(".")[0]}]({writepath})'+ "\n")


if __name__ == '__main__':
    sidebar = open("_sidebar.md", 'w')
    get_all_files_and_directories(c, 0)
    sidebar.close()
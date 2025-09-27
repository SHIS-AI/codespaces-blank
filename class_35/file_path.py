import os
dir_name='new_folder'
file_name= 'new_file.txt'
file_path = os.path.join(os.getcwd(),dir_name,file_name)
print(file_path)
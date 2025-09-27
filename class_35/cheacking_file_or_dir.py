import os
file='example.txt'
if os.path.isfile(file):
    print(f"this file {file} is a file")

elif os.path.isdir(file):
    print(f"this file {file} is a directory.")
else:
    print(f"this file {file} is not a file or directory.") 
        

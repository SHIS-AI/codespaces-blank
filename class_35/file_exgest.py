import os
file='example1.txt'
if os.path.exists(file):
    print(f"this file {file} is exists")

else:
    print(f"this file {file} is not exists")
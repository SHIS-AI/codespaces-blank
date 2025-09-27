with open('example.txt', 'r') as file:
    content = file.read()

with open('copy_op_example.txt', 'w') as file:
    file.write(content)
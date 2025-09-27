with open('example.txt', 'w+') as file:
    file.write("\nyou are awesome")
    file.seek(0)
    content= file.read()
    print(content)
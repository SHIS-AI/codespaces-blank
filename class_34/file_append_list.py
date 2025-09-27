lines=['fast line\n' 'seconf line\n' 'thard line']
print(type(lines))

with open('example.txt', 'a') as file:
    file.writelines(lines)
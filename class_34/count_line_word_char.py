def count_line_word_char(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        line=len(lines)
        words= sum(len(line.split()) for line in lines)
        chars = sum(len(line) for line in lines)
        return line, words, chars




path='example.txt'
line, word, char = count_line_word_char(path)
print(f"linrs: {line} words: {word} chars: {char}")
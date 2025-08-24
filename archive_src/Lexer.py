class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


def Lex(code): #  What does Lexer do? -Lex
    token_list = []
    pos = 0
    line = 1
    while pos < len(code):
        char = code[pos]
        if char == '\n':
            line += 1

        if char.isspace():
            pos += 1
            continue

        if char == '#':
            while pos < len(code) and code[pos] != '\n':
                pos += 1
            continue

        if char == '\'' or char == '\"':
            last_pos = pos
            pos += 1
            while pos < len(code) and code[pos] != '\n' and code[pos] != char:
                pos += 1

            if pos == len(code) or code[pos] == '\n':
                raise Exception(f"Missing pared {char} at line {line}")

            token_list += [Token("StrLiteral", code[last_pos: pos + 1])]
            pos += 1
            continue

        if char.isalpha() or char == '_':
            last_pos = pos
            while pos < len(code) and code[pos] != '\n' and (code[pos].isalpha() or code[pos].isdigit() or code[pos] == '_'):
                pos += 1
            word = code[last_pos: pos]

            if word in ['declare', 'int', 'boolean', 'void', 'assert', 'if', 'else', 'while', 'print',
        'true', 'false', 'length']:
                token_list += [Token(word, None)]

            else:
                token_list += [Token("identifier", word)]
            continue

        if char.isdigit():
            last_pos = pos
            while pos < len(code) and code[pos] != '\n' and (code[pos].isdigit() or code[pos] == '\''):
                pos += 1

            num = code[last_pos: pos]
            token_list += [Token("NumLiteral", code[last_pos: pos])]
            continue
        if pos + 1 < len(code) and code[pos: pos + 2] in ['==', '<=', '>=', '!=', '&&', '||', '**']:
            token_list += [Token(code[pos: pos + 2], None)]
            pos += 2
            continue
        if char in ['<', '>', '+', '-', '*', '/', '%', '!', '=', ';', ',',
                '(', ')', '{', '}', '[', ']', '.']:
            token_list += [Token(char, None)]
            pos += 1
            continue
        raise Exception(f'Unexpected symbol at line {line}')
    return token_list

"""
file = open("code_examples/simple_code_#1", 'r')
file_text = ''.join(file.readlines());
print(file_text)
tokens = Lex(file_text)
dor token in tokens:
    print(token.value if token.value else token.type, end='')

file.close()
#for testing Lexer itself
"""

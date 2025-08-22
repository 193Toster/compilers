from Lexer import *
from Parser import *
from PrintVisitor import *
from Interpreter import *
# Пример использования
if __name__ == "__main__":
    # Пример кода на вашем языке
    code = """
declare return int;
declare isTrue boolean[];
declare message int;
declare ind int;
declare one int;
ind = 0;
one = 'one';
message = " We can convert str && int";
print(one * (1 + 1 ** 100000 - 1  % 1329) + message);
return = 24 / 34;
print(return ** return);
isTrue[0] = true;
isTrue[1] = 1;
isTrue[2] = 'wow';
print("isTrue:");
while (ind <= 2) {
  print(isTrue[ind]);
  ind = 1 + ind;
}

    """
    
    # Лексический анализ
    tokens = Lex(code)
    
    # Синтаксический анализ
    parser = Parser(tokens)
    ast = parser.parse_programm()
    
    # Печать AST
    printer = PrintVisitor()
    print("=== AST ===")
    print(printer.visit(ast))
    
    # Интерпретация
    print("\n=== Execution ===")
    interpreter = Interpreter()
    interpreter.visit(ast)

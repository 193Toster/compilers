from antlr4 import *
from python4Lexer import python4Lexer
from python4Parser import python4Parser
from python4PrintVisitor import *
from python4Interpreter import *

def print_code(code):
    print("=== AST ===")
    PrintVisitor().visit(python4Parser(CommonTokenStream(python4Lexer(InputStream(code)))).program())

def interpret_code(code):
    print("=== Execute ===")
    Interpreter().visit(python4Parser(CommonTokenStream(python4Lexer(InputStream(code)))).program())


code = """
declare x int;
declare y int[];
x = 10;
y[2] = 5;
print(x);
x = 0;
while (x < 4) {
  print(y[x]);
 x=  x + 1;;;;
}
print(x);
"""

print_code(code)
print("")
interpret_code(code)

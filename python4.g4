grammar python4;

program: statement* EOF;

statement: variableDeclaration
         | assertStatement
         | ifStatement
         | whileStatement
         | printStatement
         | assignment
         | ';'  // empty statement
         ;

variableDeclaration: 'declare' IDENTIFIER type ';';
type: simpleType | arrayType;
simpleType: 'int' | 'boolean' | 'void';
arrayType: simpleType '[' ']';

assertStatement: 'assert' '(' exp ')' ';';
ifStatement: 'if' '(' exp ')' block ('else' block)?;
block: '{' statement* '}' | statement;
whileStatement: 'while' '(' exp ')' block;
printStatement: 'print' '(' exp ')' ';';
assignment: lvalue '=' exp ';';

lvalue: IDENTIFIER | IDENTIFIER '[' exp ']';

exp: exp op exp
    | exp '[' exp ']'
    | exp '.' 'length'
    | '!' exp
    | '(' exp ')'
    | INTEGER
    | IDENTIFIER
    | 'true'
    | 'false'
    ;

op: '&&' | '||' | '<' | '>' | '<=' | '>=' | '!=' | '==' | '+' | '-' | '*' | '/' | '%' | '**';

INTEGER: [0-9]+;
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;

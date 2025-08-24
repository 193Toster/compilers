```# compilers
Язык задается простоя грамматикой:

<program> ::=	<statement>*

<variable declaration> ::=	declare <identifier> <type>;
<simple type> ::=	int | boolean | void 
<array type> ::=	<simple type> "[" "]"

<type> ::=	<simple type> | <array type>


<statement> ::=	; | assert "(" exp ")"  | 
                <variable declaration>  | 
                if  "(" <exp> ")" block  | 
                if  "(" <exp> ")" block else block  | 
                while  "(" <exp> ")" block  | 
                print "(" <exp> ")" ";"  | 
                <lvalue> "=" <exp> ";"

<block> ::= statement | '{' statement* '}'
<lvalue> ::=	<identifier> | <identifier> "[" <exp> "]"

<exp> ::=	<exp> <op> <exp>  | 
            <exp> "[" <exp> "]"  | 
            <exp> "." length| 
            "!" <exp>  | 
            "(" <exp> ")"  | <integer literal>  | 
            <identifier>  | 
             true  | false    


<op> ::=	"&&"  |  "||"  |  "<"  |  ">"  |  "<="  |  ">="  |  "!="  |  "=="   | "+"   |  "-"   | "*"  | "/"  | "%" | "**" | 



В MannualTest.py проверяется работа Обоих виcитеров на простом примере кода.


# compilers
Язык задается простоя грамматикой:

<program> ::=	<statement>*

<variable declaration> ::=	declare <identifier> <type>;
<simple type> ::=	int | boolean | void 
<array type> ::=	<simple type> "[" "]"

<type> ::=	<simple type> | <array type>


<statement> ::=	<statement><statment> | ; | assert "(" expr ")"  | 
                <variable declaration>  | 
                if  "(" <expr> ")" "{"<statement>"}"  | 
                if  "(" <expr> ")" "{"<statement>"}" else "{<statement>}"  | 
                while  "(" <expr> ")" "{"<statement>"}"  | 
                print "(" <expr> ")" ";"  | 
                <lvalue> "=" <expr> ";"


<lvalue> ::=	<identifier> | <identifier> "[" <expr> "]"

<expr> ::=	<expr> <binary operator> <expr>  | 
            <expr> "[" <expr> "]"  | 
            <expr> "." length| 
            "!" <expr>  | 
            "(" <expr> ")"  | <integer literal>  | 
            <identifier>  | 
             true  | false    


<binary operator> ::=	"&&"   |  "||"   |  "<"   |<program> ::=	<statement>*

<variable declaration> ::=	declare <identifier> <type>;
<simple type> ::=	int | boolean | void 
<array type> ::=	<simple type> "[" "]"

<type> ::=	<simple type> | <array type>


<statement> ::=	assert "(" expr ")"  | 
                <variable declaration>  | 
                if  "(" <expr> ")" "{"<statement>"}"  | 
                if  "(" <expr> ")" "{"<statement>"}" else "{<statement>}"  | 
                while  "(" <expr> ")" "{"<statement>"}"  | 
                print "(" <expr> ")" ";"  | 
                <lvalue> "=" <expr> ";"


<lvalue> ::=	<identifier> | <identifier> "[" <expr> "]"

<expr> ::=	<expr> <binary operator> <expr>  | 
            <expr> "[" <expr> "]"  | 
            <expr> "." length| 
            "!" <expr>  | 
            "(" <expr> ")"  | <integer literal>  | 
            <identifier>  | 
             true  | false  | 
            <method invocation>    


<binary operator> ::=	"&&"   |  "||"   |  "<"   | ">"   |  "=="   | "+"   |  "-"   | "*"  | "/"  | "%"
<program> ::=	<statement>*

<variable declaration> ::=	declare <identifier> <type>;
<simple type> ::=	int | boolean | void 
<array type> ::=	<simple type> "[" "]"

<type> ::=	<simple type> | <array type>


<statement> ::=	assert "(" expr ")"  | 
                <variable declaration>  | 
                if  "(" <expr> ")" "{"<statement>"}"  | 
                if  "(" <expr> ")" "{"<statement>"}" else "{<statement>}"  | 
                while  "(" <expr> ")" "{"<statement>"}"  | 
                print "(" <expr> ")" ";"  | 
                <lvalue> "=" <expr> ";"


<lvalue> ::=	<identifier> | <identifier> "[" <expr> "]"

<expr> ::=	<expr> <binary operator> <expr>  | 
            <expr> "[" <expr> "]"  | 
            <expr> "." length| 
            "!" <expr>  | 
            "(" <expr> ")"  | <integer literal>  | 
            <identifier>  | 
             true  | false  | 
            <method invocation>    


<binary operator> ::=	"&&"   |  "||"   |  "<"   | ">"   | "<="   | ">="   |<program> ::=	<statement>*

<variable declaration> ::=	declare <identifier> <type>;
<simple type> ::=	int | boolean | void 
<array type> ::=	<simple type> "[" "]"

<type> ::=	<simple type> | <array type>


<statement> ::=	assert "(" expr ")"  | 
                <variable declaration>  | 
                if  "(" <expr> ")" "{"<statement>"}"  | 
                if  "(" <expr> ")" "{"<statement>"}" else "{<statement>}"  | 
                while  "(" <expr> ")" "{"<statement>"}"  | 
                print "(" <expr> ")" ";"  | 
                <lvalue> "=" <expr> ";"


<lvalue> ::=	<identifier> | <identifier> "[" <expr> "]"

<expr> ::=	<expr> <binary operator> <expr>  | 
            <expr> "[" <expr> "]"  | 
            <expr> "." length| 
            "!" <expr>  | 
            "(" <expr> ")"  | <integer literal>  | 
            <identifier>  | 
             true  | false  | 
            <method invocation>    


<binary operator> ::=	"&&"  |  "||"  |  "<"  |  ">"  |  "<="  |  ">="  |  "!="  |  "=="   | "+"   |  "-"   | "*"  | "/"  | "%" | "**" | 



В IntegralTest.py проверяется работа Обоих виситеров на простом премре кода.

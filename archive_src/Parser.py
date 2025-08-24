from Lexer import Token

class Type:
    pass


class Simple_Type(Type):
    def __init__(self, type):
        self.type = type


class Array_Type(Type):
    def __init__(self, type):
        self.type = type


class Expression:
    pass


class AddExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class DivExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class MulExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class NumExpression(Expression):
    def __init__(self, num):
        self.exp = num


class StrExpression(Expression):
    def __init__(self, str):
        self.exp = str


class IdExpression(Expression):
    def __init__(self, id):
        self.exp = id


class BoolExpression(Expression):
    def __init__(self, bool):
        self.exp = bool


class PowerExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class SubstractExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class ModuleExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class ieExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class neExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class gtExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class lsExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class geExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class leExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class AmpersandExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class VerticalBarExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class BracketsExpression(Expression):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2


class LengthExpression(Expression):
    def __init__(self, exp):
        self.exp = exp


class NotExpression(Expression):
    def __init__(self, exp):
        self.exp = exp


class ParanthesisExpresion(Expression):
    def __init__(self, exp):
        self.exp = exp


class Assignment:
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr


class Lvalue:
    pass


class LvalueFromId(Lvalue):
    def __init__(self, id):
        self.id = id


class LvalueFromArr(Lvalue):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp


class Statement:
    pass


class AssertStatement(Statement):
    def __init__(self, exp):
        self.exp = exp


class VariableDeclaration(Statement):
    def __init__(self, id, type):
        self.id = id
        self.type = type


class BareIfStatement(Statement):
    def __init__(self, exp, statements):
        self.exp = exp
        self.statements = statements


class IfElseStatement(Statement):
    def __init__(self, exp, statements1, statements2):
        self.exp = exp
        self.statements1 = statements1
        self.statements2 = statements2


class WhileStatement(Statement):
    def __init__(self, exp, statements):
        self.exp = exp
        self.statements = statements


class PrintStatement(Statement):
    def __init__(self, exp):
        self.exp = exp


class EmptyStatement(Statement):
    pass


class BlockStatement(Statement):
    def __init__(self, statements):
        self.statements = statements


class Programm:
    def __init__(self, statements):
        self.statements = statements


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume_token(self, expected_type=None, expected_value=None):
        token = self.current_token()
        if token is None:
            raise Exception(f"Unexpected end of input, expected {expected_type} {expected_value}")

        if expected_type is not None and token.type != expected_type:
            raise Exception(f"Expected {expected_type}, got {token.type}")

        if expected_value is not None and token.value != expected_value:
            raise Exception(f"Expected {expected_value}, got {token.value}")

        self.pos += 1
        return token

    def parse_programm(self):
        statements = []
        while self.pos < len(self.tokens):
            statement = self.parse_statement()
            if statement is not None:
                statements.append(statement)
        return Programm(statements)

    def parse_block(self):
        statements = []
        self.consume_token("{", None)
        while self.current_token() and self.current_token().type != "}":
            statement = self.parse_statement()
            if statement is not None:
                statements.append(statement)
        self.consume_token("}", None)
        return statements

    def parse_statement(self):
        token = self.current_token()
        if token is None:
            return None

        if token.type == ";":
            self.consume_token(";", None)
            return EmptyStatement()

        if token.type == "assert":
            self.consume_token("assert")
            self.consume_token("(", None)
            exp = self.parse_expression()
            self.consume_token(")", None)
            return AssertStatement(exp)

        if token.type == "declare":
            self.consume_token("declare")
            id_token = self.current_token()
            if id_token.type != "identifier":
                raise Exception("Expected identifier after declare")
            self.consume_token("identifier")
            type_token = self.current_token()
            if type_token.type not in ["int", "boolean", "void"]:
                raise Exception("Expected type after identifier")
            var_type = type_token.type
            self.consume_token(type_token.type)

            if self.current_token() and self.current_token().type == "[":
                self.consume_token("[")
                self.consume_token("]")
                var_type += "[]"

            self.consume_token(";", None)
            return VariableDeclaration(id_token.value, var_type)

        if token.type == "if":
            self.consume_token("if")
            self.consume_token("(", None)
            exp = self.parse_expression()
            self.consume_token(")", None)
            statements = self.parse_block()

            if self.current_token() and self.current_token().type == "else":
                self.consume_token("else")
                else_statements = self.parse_block()
                return IfElseStatement(exp, statements, else_statements)
            else:
                return BareIfStatement(exp, statements)

        if token.type == "while":
            self.consume_token("while")
            self.consume_token("(", None)
            exp = self.parse_expression()
            self.consume_token(")", None)
            statements = self.parse_block()
            return WhileStatement(exp, statements)

        if token.type == "print":
            self.consume_token("print")
            self.consume_token("(", None)
            exp = self.parse_expression()
            self.consume_token(")", None)
            self.consume_token(";", None)
            return PrintStatement(exp)

        try:
            saved_pos = self.pos
            lvalue = self.parse_lvalue()
            if self.current_token() and self.current_token().type == "=":
                self.consume_token("=", None)
                expr = self.parse_expression()
                self.consume_token(";", None)
                return Assignment(lvalue, expr)
            else:
                self.pos = saved_pos
        except Exception:
            self.pos = saved_pos

        raise Exception(f"Unexpected token in statement: {token.type} {token.value if hasattr(token, 'value') else ''}")

    def parse_lvalue(self):
        token = self.current_token()
        if token is None:
            raise Exception("Unexpected end of input, expected identifier in lvalue")

        if token.type != "identifier":
            raise Exception(f"Expected identifier in lvalue, got {token.type}")

        identifier = token.value
        self.consume_token("identifier")

        if self.current_token() and self.current_token().type == "[":
            self.consume_token("[")
            index_expr = self.parse_expression()
            self.consume_token("]")
            return LvalueFromArr(identifier, index_expr)
        else:
            return LvalueFromId(identifier)

    def parse_expression(self):
        return self.parse_logical_or()

    def parse_logical_or(self):
        left = self.parse_logical_and()
        while self.current_token() and self.current_token().type == "||":
            self.consume_token("||")
            right = self.parse_logical_and()
            left = VerticalBarExpression(left, right)
        return left

    def parse_logical_and(self):
        left = self.parse_equality()
        while self.current_token() and self.current_token().type == "&&":
            self.consume_token("&&")
            right = self.parse_equality()
            left = AmpersandExpression(left, right)
        return left

    def parse_equality(self):
        left = self.parse_relational()
        while self.current_token() and self.current_token().type in ["==", "!="]:
            op = self.current_token().type
            self.consume_token(op)
            right = self.parse_relational()
            if op == "==":
                left = ieExpression(left, right)
            else:
                left = neExpression(left, right)
        return left

    def parse_relational(self):
        left = self.parse_additive()
        while self.current_token() and self.current_token().type in ["<", ">", "<=", ">="]:
            op = self.current_token().type
            self.consume_token(op)
            right = self.parse_additive()
            if op == "<":
                left = lsExpression(left, right)
            elif op == ">":
                left = gtExpression(left, right)
            elif op == "<=":
                left = leExpression(left, right)
            elif op == ">=":
                left = geExpression(left, right)
        return left

    def parse_additive(self):
        left = self.parse_multiplicative()
        while self.current_token() and self.current_token().type in ["+", "-"]:
            op = self.current_token().type
            self.consume_token(op)
            right = self.parse_multiplicative()
            if op == "+":
                left = AddExpression(left, right)
            else:
                left = SubstractExpression(left, right)
        return left

    def parse_multiplicative(self):
        left = self.parse_power()
        while self.current_token() and self.current_token().type in ["*", "/", "%"]:
            op = self.current_token().type
            self.consume_token(op)
            right = self.parse_power()
            if op == "*":
                left = MulExpression(left, right)
            elif op == "/":
                left = DivExpression(left, right)
            else:
                left = ModuleExpression(left, right)
        return left

    def parse_power(self):
        left = self.parse_unary()
        while self.current_token() and self.current_token().type == "**":
            self.consume_token("**")
            right = self.parse_unary()
            left = PowerExpression(left, right)
        return left

    def parse_unary(self):
        if self.current_token() and self.current_token().type == "!":
            self.consume_token("!")
            expr = self.parse_unary()
            return NotExpression(expr)
        return self.parse_primary()

    def parse_primary(self):
        token = self.current_token()
        if token is None:
            raise Exception("Unexpected end of input in expression")

        if token.type == "NumLiteral":
            self.consume_token("NumLiteral")
            return NumExpression(int(token.value))

        if token.type == "StrLiteral":
            self.consume_token("StrLiteral")
            str_value = token.value[1:-1]
            return StrExpression(str_value)

        if token.type == "true":
            self.consume_token("true")
            return BoolExpression(True)

        if token.type == "false":
            self.consume_token("false")
            return BoolExpression(False)

        if token.type == "identifier":
            self.consume_token("identifier")
            identifier = token.value

            if self.current_token() and self.current_token().type == "[":
                self.consume_token("[")
                index_expr = self.parse_expression()
                self.consume_token("]")
                return BracketsExpression(IdExpression(identifier), index_expr)

            if self.current_token() and self.current_token().type == ".":
                self.consume_token(".")
                if not (self.current_token() and self.current_token().type == "length"):
                    raise Exception("Expected 'length' after '.'")
                self.consume_token("length")
                return LengthExpression(IdExpression(identifier))

            return IdExpression(identifier)

        if token.type == "(":
            self.consume_token("(")
            expr = self.parse_expression()
            self.consume_token(")")
            return ParanthesisExpresion(expr)

        raise Exception(f"Unexpected token in expression: {token.type}")

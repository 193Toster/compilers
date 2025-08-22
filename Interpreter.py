from Parser import *

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.array_types = {}

    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit method defined for {type(node).__name__}')

    def visit_Programm(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_BlockStatement(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_EmptyStatement(self, node):
        pass

    def visit_VariableDeclaration(self, node):
        if node.type == 'int':
            self.variables[node.id] = 0
        elif node.type == 'boolean':
            self.variables[node.id] = False
        elif node.type.endswith('[]'):
            self.variables[node.id] = []
            self.array_types[node.id] = node.type[:-2]

    def visit_AssertStatement(self, node):
        result = self.visit(node.exp)
        if not result:
            raise Exception('Assertion failed')

    def visit_BareIfStatement(self, node):
        condition = self.visit(node.exp)
        if condition:
            self.visit(BlockStatement(node.statements))

    def visit_IfElseStatement(self, node):
        condition = self.visit(node.exp)
        if condition:
            self.visit(BlockStatement(node.statements1))
        else:
            self.visit(BlockStatement(node.statements2))

    def visit_WhileStatement(self, node):
        while self.visit(node.exp):
            self.visit(BlockStatement(node.statements))

    def visit_PrintStatement(self, node):
        value = self.visit(node.exp)
        print(value)

    def visit_Assignment(self, node):
        value = self.visit(node.expr)
        lvalue = node.var

        if isinstance(lvalue, LvalueFromId):
            if lvalue.id not in self.variables:
                raise Exception(f'Undefined variable: {lvalue.id}')
            self.variables[lvalue.id] = value
        elif isinstance(lvalue, LvalueFromArr):
            if lvalue.id not in self.variables:
                raise Exception(f'Undefined variable: {lvalue.id}')
            array = self.variables[lvalue.id]
            index = self.visit(lvalue.exp)

            if not isinstance(array, list):
                raise Exception('Cannot index non-array')

            while index >= len(array):
                base_type = self.array_types.get(lvalue.id, 'int')
                if base_type == 'int':
                    array.append(0)
                elif base_type == 'boolean':
                    array.append(False)
                else:
                    array.append(None)

            array[index] = value
        else:
            raise Exception('Invalid lvalue in assignment')

    def visit_LvalueFromId(self, node):
        if node.id not in self.variables:
            raise Exception(f'Undefined variable: {node.id}')
        return self.variables[node.id]

    def visit_LvalueFromArr(self, node):
        if node.id not in self.variables:
            raise Exception(f'Undefined variable: {node.id}')
        array = self.variables[node.id]
        index = self.visit(node.exp)

        if not isinstance(array, list):
            raise Exception('Cannot index non-array')
        if index < 0 or index >= len(array):
            raise Exception('Array index out of bounds')

        return array[index]

    def visit_AddExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        if isinstance(left, str) or isinstance(right, str):
            return str(left) + str(right)
        return left + right

    def visit_DivExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        if right == 0:
            raise Exception('Division by zero')
        return left / right

    def visit_MulExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left * right

    def visit_NumExpression(self, node):
        return node.exp

    def visit_StrExpression(self, node):
        return node.exp

    def visit_IdExpression(self, node):
        if node.exp not in self.variables:
            raise Exception(f'Undefined variable: {node.exp}')
        return self.variables[node.exp]

    def visit_BoolExpression(self, node):
        return node.exp

    def visit_PowerExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left ** right

    def visit_SubstractExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left - right

    def visit_ModuleExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        if right == 0:
            raise Exception('Division by zero in modulo operation')
        return left % right

    def visit_ieExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left == right

    def visit_neExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left != right

    def visit_gtExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left > right

    def visit_lsExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left < right

    def visit_geExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left >= right

    def visit_leExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left <= right

    def visit_AmpersandExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left and right

    def visit_VerticalBarExpression(self, node):
        left = self.visit(node.exp1)
        right = self.visit(node.exp2)
        return left or right

    def visit_BracketsExpression(self, node):
        array = self.visit(node.exp1)
        index = self.visit(node.exp2)

        if not isinstance(array, list):
            raise Exception('Cannot index non-array')
        if index < 0 or index >= len(array):
            raise Exception('Array index out of bounds')

        return array[index]

    def visit_LengthExpression(self, node):
        array = self.visit(node.exp)

        if not isinstance(array, list):
            raise Exception('Cannot get length of non-array')

        return len(array)

    def visit_NotExpression(self, node):
        value = self.visit(node.exp)
        return not value

    def visit_ParanthesisExpresion(self, node):
        return self.visit(node.exp)

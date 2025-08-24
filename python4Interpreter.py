from python4Visitor import *
from python4Parser import *

class Interpreter(python4Visitor):
    def __init__(self):
        self.variables = {}

    def visitProgram(self, ctx: python4Parser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitVariableDeclaration(self, ctx: python4Parser.VariableDeclarationContext):
        var_name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.type_())

        if '[]' in var_type:
            base_type = var_type.replace('[]', '')
            self.variables[var_name] = {
                'type': base_type,
                'values': []
            }
        else:
            if var_type == 'int':
                self.variables[var_name] = 0
            elif var_type == 'boolean':
                self.variables[var_name] = False
            else:
                self.variables[var_name] = None

    def visitType_(self, ctx: python4Parser.TypeContext):
        return self.visitChildren(ctx)

    def visitSimpleType(self, ctx: python4Parser.SimpleTypeContext):
        return ctx.getText()

    def visitArrayType(self, ctx: python4Parser.ArrayTypeContext):
        base_type = self.visit(ctx.simpleType())
        return f"{base_type}[]"

    def visitAssignment(self, ctx: python4Parser.AssignmentContext):
        lvalue = self.visit(ctx.lvalue())
        value = self.visit(ctx.exp())

        if isinstance(lvalue, str):
            if lvalue in self.variables:
                self.variables[lvalue] = value
            else:
                raise NameError(f"Variable '{lvalue}' not declared")

        elif isinstance(lvalue, tuple):
            array_name, index = lvalue
            if array_name in self.variables and isinstance(self.variables[array_name], dict):
                arr = self.variables[array_name]
                while index >= len(arr['values']):
                    default_val = 0 if arr['type'] == 'int' else False
                    arr['values'].append(default_val)

                arr['values'][index] = value
            else:
                raise NameError(f"Array '{array_name}' not declared")

    def visitLvalue(self, ctx: python4Parser.LvalueContext):
        if ctx.getChildCount() == 1:
            return ctx.IDENTIFIER().getText()
        else:
            array_name = ctx.IDENTIFIER().getText()
            index = self.visit(ctx.exp())
            if not isinstance(index, int):
                raise TypeError("Array index must be an integer")
            return (array_name, index)

    def visitIfStatement(self, ctx: python4Parser.IfStatementContext):
        condition = self.visit(ctx.exp())
        if condition:
            self.visit(ctx.block(0))
        elif ctx.elseBlock:
            self.visit(ctx.block(1))

    def visitBlock(self, ctx: python4Parser.BlockContext):
        return self.visitChildren(ctx)

    def visitWhileStatement(self, ctx: python4Parser.WhileStatementContext):
        while self.visit(ctx.exp()):
            self.visit(ctx.block())

    def visitPrintStatement(self, ctx: python4Parser.PrintStatementContext):
        value = self.visit(ctx.exp())
        print(value)
        return None

    def visitExp(self, ctx: python4Parser.ExpContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())

        if ctx.IDENTIFIER():
            var_name = ctx.IDENTIFIER().getText()
            if var_name in self.variables:
                return self.variables[var_name]
            raise NameError(f"Variable '{var_name}' not declared")

        if ctx.getText() == 'true':
            return True
        if ctx.getText() == 'false':
            return False

        if ctx.getChildCount() >= 4 and ctx.getChild(1).getText() == '[':
            array_val = self.visit(ctx.exp(0))
            index = self.visit(ctx.exp(1))
            if isinstance(array_val, dict) and 'values' in array_val:
                if index < len(array_val['values']):
                    return array_val['values'][index]
                else:
                    return 0 if array_val['type'] == 'int' else False
            else:
                raise TypeError("Cannot index non-array value")

        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '.' and ctx.getChild(2).getText() == 'length':
            array_val = self.visit(ctx.exp(0))
            if isinstance(array_val, dict) and 'values' in array_val:
                return len(array_val['values'])
            else:
                raise TypeError("Cannot get length of non-array")

        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':
            return not self.visit(ctx.exp(0))

        if ctx.op() and ctx.getChildCount() == 3:
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))
            op = ctx.op().getText()

            if left is None or right is None:
                raise ValueError(f"Undefined operands in operation {op}")

            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right if right != 0 else float('inf')
            if op == '%': return left % right if right != 0 else 0
            if op == '**': return left ** right
            if op == '<': return left < right
            if op == '>': return left > right
            if op == '<=': return left <= right
            if op == '>=': return left >= right
            if op == '==': return left == right
            if op == '!=': return left != right
            if op == '&&': return left and right
            if op == '||': return left or right

        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.exp(0))

        return None

    def visitOp(self, ctx: python4Parser.OpContext):
        return ctx.getText()

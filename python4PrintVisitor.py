from python4Visitor import *
from python4Parser import *

class PrintVisitor(python4Visitor):
    def __init__(self):
        pass

    def visitProgram(self, ctx):
        result = self.visitChildren(ctx)
        return result

    def visitVariableDeclaration(self, ctx):
        var_name = ctx.IDENTIFIER().getText()
        var_type = self.visit(ctx.type_())
        print(f"declaration: {var_name} {var_type}")
        return f"{var_name} {var_type}"

    def visitType_(self, ctx):
        return self.visitChildren(ctx)

    def visitSimpleType(self, ctx):
        return ctx.getText()

    def visitArrayType(self, ctx):
        base_type = self.visit(ctx.simpleType())
        return f"{base_type}[]"

    def visitAssignment(self, ctx):
        lvalue = self.visit(ctx.lvalue())
        expr = self.visit(ctx.exp())
        print(f"{lvalue} = {expr}")
        return f"{lvalue} = {expr}"

    def visitLvalue(self, ctx):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        array_name = ctx.IDENTIFIER().getText()
        index = self.visit(ctx.exp(0))
        return f"{array_name}[{index}]"

    def visitIfStatement(self, ctx: python4Parser.IfStatementContext):
        condition = self.visit(ctx.exp())
        print(f"if ({condition}) {{")
        self.visit(ctx.block(0))
        print("}")

        if ctx.block(1) is not None:
            print("else {")
            self.indent_level += 1
            self.visit(ctx.block(1))
            self.indent_level -= 1
            print("}")
        return None

    def visitBlock(self, ctx: python4Parser.BlockContext):
        return self.visitChildren(ctx)

    def visitExp(self, ctx: python4Parser.ExpContext):
        if ctx.INTEGER():
            return ctx.INTEGER().getText()
        elif ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.getText() == 'true':
            return 'true'
        elif ctx.getText() == 'false':
            return 'false'
        elif ctx.getChildCount() == 3 and ctx.op():
            left = self.visit(ctx.exp(0))
            right = self.visit(ctx.exp(1))
            op = ctx.op().getText()
            return f"({left} {op} {right})"
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':
            expr = self.visit(ctx.exp(0))
            return f"!{expr}"
        return self.visitChildren(ctx)

    def visitPrintStatement(self, ctx: python4Parser.PrintStatementContext):
        expr = self.visit(ctx.exp())
        print(f"print({expr})")
        return None

    def visitWhileStatement(self, ctx: python4Parser.WhileStatementContext):
        condition = self.visit(ctx.exp())
        print(f"while ({condition}) {{")
        self.visit(ctx.block())
        print("}")
        return None

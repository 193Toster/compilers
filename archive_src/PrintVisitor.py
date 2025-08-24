from Parser import *
class PrintVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    
    def generic_visit(self, node):
        raise Exception(f'No visit method defined for {type(node).__name__}')
    
    def visit_Programm(self, node):
        result = ''
        for statement in node.statements:
            result += self.visit(statement) + '\n'
        return result
    
    def visit_BlockStatement(self, node):
        result = '{\n'
        for statement in node.statements:
            result += '  ' + self.visit(statement) + '\n'
        result += '}'
        return result
    
    def visit_EmptyStatement(self, node):
        return ';'
    
    def visit_VariableDeclaration(self, node):
        return f'declare {node.id} {node.type};'
    
    def visit_AssertStatement(self, node):
        return f'assert({self.visit(node.exp)});'
    
    def visit_BareIfStatement(self, node):
        return f'if ({self.visit(node.exp)}) {self.visit_BlockStatement(BlockStatement(node.statements))}'
    
    def visit_IfElseStatement(self, node):
        return f'if ({self.visit(node.exp)}) {self.visit_BlockStatement(BlockStatement(node.statements1))} else {self.visit_BlockStatement(BlockStatement(node.statements2))}'
    
    def visit_WhileStatement(self, node):
        return f'while ({self.visit(node.exp)}) {self.visit_BlockStatement(BlockStatement(node.statements))}'
    
    def visit_PrintStatement(self, node):
        return f'print({self.visit(node.exp)});'
    
    def visit_Assignment(self, node):
        return f'{self.visit(node.var)} = {self.visit(node.expr)};'
    
    def visit_LvalueFromId(self, node):
        return node.id
    
    def visit_LvalueFromArr(self, node):
        return f'{node.id}[{self.visit(node.exp)}]'
    
    def visit_AddExpression(self, node):
        return f'({self.visit(node.exp1)} + {self.visit(node.exp2)})'
    
    def visit_DivExpression(self, node):
        return f'({self.visit(node.exp1)} / {self.visit(node.exp2)})'
    
    def visit_MulExpression(self, node):
        return f'({self.visit(node.exp1)} * {self.visit(node.exp2)})'
    
    def visit_NumExpression(self, node):
        return str(node.exp)
    
    def visit_StrExpression(self, node):
        return f'"{node.exp}"'
    
    def visit_IdExpression(self, node):
        return node.exp
    
    def visit_BoolExpression(self, node):
        return 'true' if node.exp else 'false'
    
    def visit_PowerExpression(self, node):
        return f'({self.visit(node.exp1)} ** {self.visit(node.exp2)})'
    
    def visit_SubstractExpression(self, node):
        return f'({self.visit(node.exp1)} - {self.visit(node.exp2)})'
    
    def visit_ModuleExpression(self, node):
        return f'({self.visit(node.exp1)} % {self.visit(node.exp2)})'
    
    def visit_ieExpression(self, node):
        return f'({self.visit(node.exp1)} == {self.visit(node.exp2)})'
    
    def visit_neExpression(self, node):
        return f'({self.visit(node.exp1)} != {self.visit(node.exp2)})'
    
    def visit_gtExpression(self, node):
        return f'({self.visit(node.exp1)} > {self.visit(node.exp2)})'
    
    def visit_lsExpression(self, node):
        return f'({self.visit(node.exp1)} < {self.visit(node.exp2)})'
    
    def visit_geExpression(self, node):
        return f'({self.visit(node.exp1)} >= {self.visit(node.exp2)})'
    
    def visit_leExpression(self, node):
        return f'({self.visit(node.exp1)} <= {self.visit(node.exp2)})'
    
    def visit_AmpersandExpression(self, node):
        return f'({self.visit(node.exp1)} && {self.visit(node.exp2)})'
    
    def visit_VerticalBarExpression(self, node):
        return f'({self.visit(node.exp1)} || {self.visit(node.exp2)})'
    
    def visit_BracketsExpression(self, node):
        return f'{self.visit(node.exp1)}[{self.visit(node.exp2)}]'
    
    def visit_LengthExpression(self, node):
        return f'{self.visit(node.exp)}.length'
    
    def visit_NotExpression(self, node):
        return f'!{self.visit(node.exp)}'
    
    def visit_ParanthesisExpresion(self, node):
        return f'({self.visit(node.exp)})'

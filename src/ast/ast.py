class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, functions):
        self.functions = functions

class Function(ASTNode):
    def __init__(self, name, params, return_type, body, is_public=False):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.body = body
        self.is_public = is_public

class Parameter(ASTNode):
    def __init__(self, name, param_type):
        self.name = name
        self.param_type = param_type

class IfStatement(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class ReturnStatement(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class BinaryOperation(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class Number(ASTNode):
    def __init__(self, value):
        self.value = int(value)  # Ensure the value is stored as an integer

class Identifier(ASTNode):
    def __init__(self, value):
        self.value = value

class VariableReference(ASTNode):
    def __init__(self, name):
        self.name = name
from lexer.lexer import Lexer, Token
from ast.ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def eat(self, token_type):
        if self.tokens[self.current_token_index].type != token_type:
            raise Exception(f"Unexpected token: {self.tokens[self.current_token_index].type}, expected: {token_type}")
        self.current_token_index += 1

    def parse(self):
        return self.program()

    def program(self):
        functions = []
        while self.current_token_index < len(self.tokens):
            token_type = self.tokens[self.current_token_index].type
            if token_type == 'KEYWORD_FN':
                functions.append(self.main_function_definition() if self.peek('KEYWORD_PUB') else self.function_definition())
            else:
                self.current_token_index += 1  # Skip unexpected tokens
        return Program(functions)

    def peek(self, token_type, offset=1):
        peek_index = self.current_token_index + offset
        return peek_index < len(self.tokens) and self.tokens[peek_index].type == token_type

    def function_definition(self):
        self.eat('KEYWORD_FN')
        name = self.tokens[self.current_token_index].value
        self.eat('IDENT')
        self.eat('LPAREN')
        params = self.parameters()
        self.eat('RPAREN')
        self.eat('ARROW')
        return_type = self.tokens[self.current_token_index].value
        self.eat('INT_TYPE')
        self.eat('LBRACE')
        body = self.function_body()
        self.eat('RBRACE')
        return Function(name, params, return_type, body, False)

    def main_function_definition(self):
        self.eat('KEYWORD_FN')
        self.eat('KEYWORD_PUB')
        return self.function_definition(True)

    def parameters(self):
        params = []
        while self.tokens[self.current_token_index].type != 'RPAREN':
            param_name = self.tokens[self.current_token_index].value
            self.eat('IDENT')
            self.eat('COLON')
            param_type = self.tokens[self.current_token_index].value
            self.eat('INT_TYPE')
            params.append(Parameter(param_name, param_type))
            if self.tokens[self.current_token_index].type == 'COMMA':
                self.eat('COMMA')
        return params

    def function_body(self):
        body = []
        while self.tokens[self.current_token_index].type != 'RBRACE':
            token_type = self.tokens[self.current_token_index].type
            if token_type == 'KEYWORD_IF':
                body.append(self.if_function())
            elif token_type == 'KEYWORD_RETURN':
                body.append(self.return_function())
            elif token_type == 'IDENT' and self.peek('ASSIGN'):
                body.append(self.variable_assignment())
            elif token_type == 'KEYWORD_PRINTLN':
                body.append(self.print_function())
            else:
                self.current_token_index += 1  # Skip unexpected tokens
        return body

    def variable_assignment(self):
        var_name = self.tokens[self.current_token_index].value
        self.eat('IDENT')
        self.eat('ASSIGN')
        expression = self.expression()
        return Assignment(var_name, 'int', expression)

    def return_function(self):
        self.eat('KEYWORD_RETURN')
        return ReturnStatement(self.expression())

    def if_function(self):
        self.eat('KEYWORD_IF')
        condition = self.expression()

        if not self.peek('LBRACE'):
            raise SyntaxError("Expected '{' after condition in 'if' statement")
        self.eat('LBRACE')
        then_branch = self.function_body()
        self.eat('RBRACE')

        else_branch = None
        if self.peek('KEYWORD_ELSE'):
            self.eat('KEYWORD_ELSE')
            if self.peek('KEYWORD_IF'):
                else_branch = [self.if_function()]
            elif self.peek('LBRACE'):
                self.eat('LBRACE')
                else_branch = self.function_body()
                self.eat('RBRACE')
            else:
                raise SyntaxError("Expected '{' after 'else'")

        return IfStatement(condition, then_branch, else_branch)

    def print_function(self):
        self.eat('KEYWORD_PRINTLN')
        self.eat('LPAREN')
        expression = self.expression()
        self.eat('RPAREN')
        return PrintStatement(expression)

    def expression(self):
        token = self.tokens[self.current_token_index]
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return NumberLiteral(int(token.value))
        elif token.type in ['LESS_THAN', 'GREATER_THAN', 'EQUALS']:
            comparison_operator = token.type
            self.eat(token.type)
            left = self.expression()
            right = self.expression()
            return ComparisonOperation(comparison_operator, left, right)
        elif token.type in ['PLUS', 'MINUS', 'MUL', 'DIV']:
            self.eat(token.type)
            left = self.expression()
            right = self.expression()
            return BinaryOperation(token.type, left, right)
        elif token.type == 'IDENT':
            self.eat('IDENT')
            return VariableReference(token.value)
        elif token.type in ['TRUE', 'FALSE']:
            self.eat(token.type)
            return BooleanLiteral(token.type == 'TRUE')
        else:
            raise Exception(f"Unexpected token in expression: {token.type}")
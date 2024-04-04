from lexer.lexer import Lexer, Token
from ast.ast import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def eat(self, token_type):
        if self.tokens[self.current_token_index].type == token_type:
            self.current_token_index += 1
        else:
            raise Exception(f"Unexpected token: {self.tokens[self.current_token_index].type}, expected: {token_type}")

    def parse(self):
        return self.program()

    def program(self):
        functions = []
        while self.current_token_index < len(self.tokens):
            if self.tokens[self.current_token_index].type == 'KEYWORD_FN':
                functions.append(self.function())
            else:
                self.current_token_index += 1  # Skip unexpected tokens
        return Program(functions)

    def function(self):
        self.eat('KEYWORD_FN')
        is_public = False
        if self.tokens[self.current_token_index].type == 'KEYWORD_PUB':
            is_public = True
            self.eat('KEYWORD_PUB')
        name = self.tokens[self.current_token_index].value
        self.eat('IDENT')  # function name
        self.eat('LPAREN')
        # Skipping parameters parsing for simplicity
        self.eat('RPAREN')
        self.eat('ARROW')
        return_type = self.tokens[self.current_token_index].value
        self.eat('INT_TYPE')  # Assuming return type is always int for simplicity
        self.eat('LBRACE')
        body = []
        while self.tokens[self.current_token_index].type != 'RBRACE':
            if self.tokens[self.current_token_index].type == 'KEYWORD_IF':
                body.append(self.if_statement())
            elif self.tokens[self.current_token_index].type == 'KEYWORD_RETURN':
                body.append(self.return_statement())
            else:
                self.current_token_index += 1  # Skip unexpected tokens
        self.eat('RBRACE')
        return Function(name, [], return_type, body, is_public)  # Simplified: no params

    def if_statement(self):
        self.eat('KEYWORD_IF')
        condition = self.expression()
        then_branch = []
        while self.tokens[self.current_token_index].type != 'KEYWORD_RETURN':
            self.current_token_index += 1  # Skip to return statement for simplicity
        then_branch.append(self.return_statement())
        return IfStatement(condition, then_branch)

    def return_statement(self):
        self.eat('KEYWORD_RETURN')
        expression = self.expression()
        self.eat('SEMICOL')
        return ReturnStatement(expression)

    def expression(self):
        # This is a simplified version. You should implement proper expression parsing.
        left = self.term()
        while self.tokens[self.current_token_index].type in ('PLUS', 'MINUS'):
            operator = self.tokens[self.current_token_index].type
            self.eat(operator)
            right = self.term()
            left = BinaryOperation(left, operator, right)
        return left

    def term(self):
        token = self.tokens[self.current_token_index]
        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        elif token.type == 'IDENT':
            self.eat('IDENT')
            return Identifier(token.value)
        else:
            raise Exception("Unexpected token type")
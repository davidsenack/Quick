from lexer import Lexer, Token
from ast import *

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
            functions.append(self.function())
        return Program(functions)

    def function(self):
        self.eat('IDENT')  # 'fn'
        name = self.tokens[self.current_token_index].value
        self.eat('IDENT')  # function name
        self.eat('LPAREN')
        # Skipping parameters parsing for simplicity
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = []
        while self.tokens[self.current_token_index].type != 'RBRACE':
            if self.tokens[self.current_token_index].type == 'IDENT' and self.tokens[self.current_token_index + 1].value == 'if':
                body.append(self.if_statement())
            else:
                body.append(self.return_statement())
        self.eat('RBRACE')
        return Function(name, [], 'int', body)  # Simplified: no params, return type always int

    def if_statement(self):
        self.eat('IDENT')  # 'if'
        condition = self.expression()
        then_branch = self.return_statement()
        return IfStatement(condition, then_branch)

    def return_statement(self):
        self.eat('IDENT')  # 'return'
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

# Example usage
if __name__ == '__main__':
    lexer = Lexer('''
    fn fibonacci(n: int) -> int {

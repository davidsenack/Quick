import re

# Token types
TOKEN_TYPES = [
    ('NUMBER',   r'\d+'),
    ('IDENT',    r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ASSIGN',   r'='),
    ('SEMICOL',  r';'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('LBRACE',   r'\{'),
    ('RBRACE',   r'\}'),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('NEWLINE',  r'\n'),
    ('SKIP',     r'[ \t]+'),  # Skip over spaces and tabs
    ('MISMATCH', r'.'),       # Any other character
]

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {repr(self.value)})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.text):
            for token_type, pattern in TOKEN_TYPES:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    if token_type != 'SKIP':
                        value = match.group(0)
                        self.tokens.append(Token(token_type, value))
                    self.pos = match.end()
                    break
            else:
                raise SyntaxError(f'Illegal character: {self.text[self.pos]}')
        return self.tokens

# Example usage
if __name__ == '__main__':
    input_code = '''
    fn fibonacci(n: int) -> int {
        if n <= 2 {
            return n
        }
        return fibonacci(n-1) + fibonacci(n-2)
    }
    '''

    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
import re

# Token types
TOKEN_TYPES = [
    # Keywords
    ('KEYWORD_FN', r'\bfn\b'),  # Keyword for function declaration
    ('KEYWORD_PUB', r'\bpub\b'),  # Keyword for public function declaration
    ('KEYWORD_VAR', r'\bvar\b'),  # Keyword for variable declaration
    ('KEYWORD_IF', r'\bif\b'),  # Keyword for if statement
    ('KEYWORD_RETURN', r'\breturn\b'),  # Keyword for return statement
    ('KEYWORD_PRINTLN', r'\bprintln\b'),  # Keyword for println function
    # Types
    ('INT_TYPE', r'\bint\b'),  # Integer type declaration
    # Operators and punctuation
    ('ASSIGN', r'='),  # Assignment operator
    ('ARROW', r'->'),  # Arrow used in function return type declaration
    ('LESS_THAN', r'<'),
    ('GREATER_THAN', r'>'),
    ('SEMICOL', r';'),  # Semicolon
    ('COLON', r':'),  # Colon character
    ('LPAREN', r'\('),  # Left parenthesis
    ('RPAREN', r'\)'),  # Right parenthesis
    ('LBRACE', r'\{'),  # Left brace
    ('RBRACE', r'\}'),  # Right brace
    ('PLUS', r'\+'),  # Plus operator
    ('MINUS', r'-'),  # Minus operator
    ('MUL', r'\*'),  # Multiplication operator
    ('DIV', r'/'),  # Division operator
    # Other
    ('NUMBER', r'\d+'),  # Number
    ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identifier
    ('NEWLINE', r'\n'),  # Newline
    ('SKIP', r'[ \t\r]+'),  # Skip over spaces, tabs, and carriage returns
    # Removed MISMATCH token to avoid catching valid characters in incorrect contexts
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
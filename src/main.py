import os
from lexer import Lexer
from parser import Parser
from transpiler import Transpiler

def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_output_file(content, filename):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(filename, 'w') as file:
        file.write(content)

def main():
    # Step 1: Read the input file
    input_filename = 'input/fibonacci.quick'
    input_code = read_input_file(input_filename)
    
    # Step 2: Tokenize the input
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    
    # Step 3: Parse the tokens into an AST
    parser = Parser(tokens)
    ast = parser.parse()
    
    # Step 4: Transpile the AST into C code
    transpiler = Transpiler()
    c_code = transpiler.transpile(ast)
    
    # Step 5: Write the output C code
    output_filename = 'output/output.c'
    write_output_file(c_code, output_filename)
    
    print(f'Transpiled C code has been written to {output_filename}')

if __name__ == '__main__':
    main()
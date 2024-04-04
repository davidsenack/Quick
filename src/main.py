import os
import sys
import subprocess

from lexer.lexer import Lexer
from parser.parser import Parser
from transpiler.transpiler import Transpiler

def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_output_file(content, filename):
    output_dir = os.path.dirname(filename)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(filename, 'w') as file:
        file.write(content)

def compile_c_code(c_file_path, output_executable_name):
    try:
        subprocess.run(['gcc', '-Ofast', c_file_path, '-o', output_executable_name, '-lgmp'], check=True)
        print(f"Compiled successfully. Executable: {output_executable_name}")
    except subprocess.CalledProcessError as e:
        print(f"Compilation failed: {e}")

def build_project(project_name):
    # Step 1: Read the input file
    input_filename = f'examples/{project_name}.quick'  # Changed path to match the new location
    # print(os.path.abspath(input_filename))  # Add this line to print the absolute path
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
    output_filename = f'output/{project_name}.c'  # Assuming output directory is at the root
    write_output_file(c_code, output_filename)
    
    # Compile the generated C code
    executable_name = f'output/{project_name}'
    compile_c_code(output_filename, executable_name)

    print(f'Transpiled C code has been written to {output_filename}')

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "build":
        print("Usage: quick build <project_name>")
        sys.exit(1)
    project_name = sys.argv[2]
    build_project(project_name)

if __name__ == '__main__':
    main()
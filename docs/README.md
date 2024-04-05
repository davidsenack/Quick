# Quick Programming Language

Welcome to the Quick programming language project. Quick is a simple, yet powerful programming language designed to make the process of writing code as efficient and enjoyable as possible. This project includes a lexer, parser, and transpiler that work together to convert Quick code into C code, which can then be compiled and executed. With the integration of GNU's MP library for arbitrary precision arithmetic, Quick combines the speed benefits of C with the ease of writing clear, type-annotated code.

## Features

- **Simple Syntax**: Quick's syntax is designed to be easy to read and write, making programming a breeze.
- **Transpilation to C with Arbitrary Precision Arithmetic**: Quick code is transpiled into C, leveraging the GNU MP library for high-performance arithmetic operations beyond standard precision, ensuring compatibility with C libraries.
- **Support for Recursive Functions**: Write complex algorithms easily with support for recursive function calls.
- **Conditional Statements**: Includes support for `if` statements, enabling conditional logic in your programs.
- **Variable Declarations**: Declare variables with ease using the `var` keyword, with clear type annotations for maintainability and readability.

## Getting Started

To get started with Quick, clone this repository and navigate to the `src` directory. From there, you can run the `main.py` script to build and compile Quick programs, taking advantage of the integrated arbitrary precision arithmetic for your computational needs.

### Building a Quick Program

1. Write your Quick program in a `.quick` file. For example, see the `examples/fibonacci.quick` file for a Fibonacci sequence generator that benefits from arbitrary precision arithmetic.
2. Run the build command: `python main.py build <project_name>`, where `<project_name>` is the name of your Quick program without the `.quick` extension.
3. The build process will transpile your Quick code into C, compile it using the GNU MP library, and generate an executable in the `output` directory.

## Example

Here's a simple Quick program that calculates the Fibonacci sequence:

```gleam
fn fibonacci(n: int) -> int {
    var a: int = 0
    var b: int = 1
    
    for _ in 0..n-2 {
        var c: int = a + b
        a = b
        b = c
    }
    return b
}

fn pub main() -> int {
    var x: int = 1 000 000 
    fibonacci(x)
    return 0
}

```
```bash
**david@quicklang:~$** quick build fibonacci
**david@quicklang:~$** time ./fibonacci

real    0m5.487s
user    0m5.487s
sys     0m0.000s
```

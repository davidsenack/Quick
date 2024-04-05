# Quick Programming Language

Welcome to the Quick programming language project. Quick is a simple, yet powerful programming language designed to make the process of writing code as efficient and enjoyable as possible. This project includes a lexer, parser, and transpiler that work together to convert Quick code into C code, which can then be compiled and executed.

## Features

- **Simple Syntax**: Quick's syntax is designed to be easy to read and write, making programming a breeze.
- **Transpilation to C**: Quick code is transpiled into C, allowing for high performance and compatibility with C libraries.
- **Support for Recursive Functions**: Write complex algorithms easily with support for recursive function calls.
- **Conditional Statements**: Includes support for `if` statements, enabling conditional logic in your programs.
- **Variable Declarations**: Declare variables with ease using the `var` keyword.

## Getting Started

To get started with Quick, clone this repository and navigate to the `src` directory. From there, you can run the `main.py` script to build and compile Quick programs.

### Building a Quick Program

1. Write your Quick program in a `.quick` file. For example, see the `examples/fibonacci.quick` file for a Fibonacci sequence generator.
2. Run the build command: `python main.py build <project_name>`, where `<project_name>` is the name of your Quick program without the `.quick` extension.
3. The build process will transpile your Quick code into C, compile it, and generate an executable in the `output` directory.

## Example

Here's a simple Quick program that calculates the Fibonacci sequence:

```gleam
fn fibonacci(n: int) -> int {
    if n < 2 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

fn pub main() -> int {
    var x: int = 10
    println(fibonacci(x))
    return 0
}

```
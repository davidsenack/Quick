from ast import *
import os 

class Transpiler:
    def __init__(self):
        self.output = ['#include<stdio.h>\n']  # Include stdio.h at the beginning of the output

    def transpile(self, node):
        method_name = 'transpile_' + type(node).__name__
        method = getattr(self, method_name, self.generic_transpile)
        method_output = method(node)
        if method_output is not None:
            self.output.append(method_output)
        return method_output

    def generic_transpile(self, node):
        raise Exception(f'No transpile_ method defined for {type(node).__name__}')

    def transpile_Program(self, node):
        for function in node.functions:
            self.transpile(function)
        # No hardcoded main function, rely on AST
        return '\n'.join(self.output)

    def transpile_Function(self, node):
        header = f'int {node.name}('
        params_code = ', '.join([f'int {param[0]}' for param in node.params])  # param is a tuple (name, type)
        header += params_code + ') {\n'
        body = '\n'.join([self.transpile(statement) for statement in node.body])
        footer = '\n}\n'
        function_output = header + body + footer
        return function_output

    def transpile_IfStatement(self, node):
        condition = self.transpile(node.condition)
        then_branch = '\n'.join([self.transpile(statement) for statement in node.then_branch])
        if_statement_output = f'if ({condition}) {{\n{then_branch}\n}}\n'
        return if_statement_output

    def transpile_ReturnStatement(self, node):
        expression = self.transpile(node.expression)
        return_statement_output = f'return {expression};\n'  # Ensure newline is added for proper formatting
        return return_statement_output

    def transpile_BinaryOperation(self, node):
        left = self.transpile(node.left)
        right = self.transpile(node.right)
        operator = node.operator
        binary_operation_output = f'{left} {operator} {right}'  # Adjusted for standard C operation
        return binary_operation_output

    def transpile_Number(self, node):
        number_output = f'{node.value}'  # Removed unnecessary semicolon
        return number_output

    def transpile_Identifier(self, node):
        identifier_output = node.value
        return identifier_output
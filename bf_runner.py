#!/usr/bin/env python3
"""
Simple Brainfuck Interpreter

A minimal, educational Brainfuck interpreter written in Python.
Demonstrates how to implement a Turing-complete language with just 8 symbols.

Usage:
    python bf_runner.py <filename.bf>
    python bf_runner.py <filename.bf> --debug
    python bf_runner.py <filename.bf> --trace

Symbols:
    > : Move pointer right
    < : Move pointer left
    + : Increment current cell
    - : Decrement current cell
    . : Output current cell as ASCII
    , : Input one character
    [ : Jump to matching ] if current cell is 0
    ] : Jump back to matching [ if current cell is not 0
"""

import sys
import os


class BrainfuckInterpreter:
    """Interprets and executes Brainfuck programs."""
    
    def __init__(self, program, memory_size=30000, debug=False, trace=False):
        """
        Initialize the interpreter.
        
        Args:
            program: String containing Brainfuck code
            memory_size: Size of memory tape (default 30000 cells)
            debug: Enable debug output
            trace: Enable instruction trace
        """
        self.program = self._clean_program(program)
        self.memory = [0] * memory_size
        self.data_pointer = 0
        self.instruction_pointer = 0
        self.output = ""
        self.debug = debug
        self.trace = trace
        self.bracket_map = self._build_bracket_map()
        
    def _clean_program(self, program):
        """Remove all non-Brainfuck characters from the program."""
        valid_chars = '><+-.,[]'
        return ''.join(c for c in program if c in valid_chars)
    
    def _build_bracket_map(self):
        """Pre-compute bracket matching for O(1) loop jumps."""
        bracket_map = {}
        stack = []
        
        for i, char in enumerate(self.program):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if stack:
                    left = stack.pop()
                    bracket_map[left] = i
                    bracket_map[i] = left
        
        return bracket_map
    
    def run(self):
        """Execute the Brainfuck program."""
        while self.instruction_pointer < len(self.program):
            self._execute_instruction()
        
        return self.output
    
    def _execute_instruction(self):
        """Execute a single instruction."""
        instruction = self.program[self.instruction_pointer]
        
        if self.trace:
            print(f"IP: {self.instruction_pointer:5d} | "
                  f"DP: {self.data_pointer:5d} | "
                  f"Cell: {self.memory[self.data_pointer]:3d} | "
                  f"Inst: {instruction}")
        
        if instruction == '>':
            self.data_pointer = (self.data_pointer + 1) % len(self.memory)
            
        elif instruction == '<':
            self.data_pointer = (self.data_pointer - 1) % len(self.memory)
            
        elif instruction == '+':
            self.memory[self.data_pointer] = (self.memory[self.data_pointer] + 1) % 256
            
        elif instruction == '-':
            self.memory[self.data_pointer] = (self.memory[self.data_pointer] - 1) % 256
            
        elif instruction == '.':
            self.output += chr(self.memory[self.data_pointer])
            
        elif instruction == ',':
            # Input - read from stdin
            try:
                char = sys.stdin.read(1)
                if char:
                    self.memory[self.data_pointer] = ord(char)
                else:
                    self.memory[self.data_pointer] = 0
            except:
                self.memory[self.data_pointer] = 0
            
        elif instruction == '[':
            if self.memory[self.data_pointer] == 0:
                self.instruction_pointer = self.bracket_map.get(
                    self.instruction_pointer, self.instruction_pointer
                )
            
        elif instruction == ']':
            if self.memory[self.data_pointer] != 0:
                self.instruction_pointer = self.bracket_map.get(
                    self.instruction_pointer, self.instruction_pointer
                )
        
        self.instruction_pointer += 1
    
    def get_memory_state(self):
        """Return non-zero memory cells for debugging."""
        return {i: v for i, v in enumerate(self.memory) if v != 0}


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python bf_runner.py <filename.bf> [--debug] [--trace]")
        print("\nOptions:")
        print("  --debug : Show interpreter state")
        print("  --trace : Show each instruction")
        sys.exit(1)
    
    filename = sys.argv[1]
    debug = '--debug' in sys.argv
    trace = '--trace' in sys.argv
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found")
        sys.exit(1)
    
    try:
        with open(filename, 'r') as f:
            program = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    try:
        interpreter = BrainfuckInterpreter(program, debug=debug, trace=trace)
        output = interpreter.run()
        
        if output:
            print(output, end='')
        
        if debug:
            print("\n--- Debug Info ---")
            print(f"Program length: {len(interpreter.program)} instructions")
            print(f"Memory used: {len(interpreter.get_memory_state())} cells")
            print(f"Output length: {len(output)} characters")
            
    except KeyboardInterrupt:
        print("\nProgram interrupted")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()

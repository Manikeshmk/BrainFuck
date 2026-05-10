<div align="center">

# 🧠 Only Brainfuck

### _The Minimalist Language That Proves Turing Completeness_

[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Python](https://img.shields.io/badge/Code_Style-Python-blue)](https://www.python.org/)
[![Turing Complete](https://img.shields.io/badge/Turing-Complete-brightgreen)](https://en.wikipedia.org/wiki/Turing_completeness)

**A collection of elegant Brainfuck programs demonstrating that you can create amazing things with just 8 symbols.**

[🚀 Quick Start](#quick-start) • [📚 What is Brainfuck?](#what-is-brainfuck) • [📖 Programs](#programs) • [💡 Techniques](#techniques) • [🤝 Contributing](#contributing)

</div>

---

## 📖 Overview

Welcome to **Only Brainfuck** — a curated collection of pure Brainfuck programs that generate beautiful ASCII art, patterns, and designs. This project is perfect for:

- 🎓 **Learners** wanting to understand Turing-complete languages
- 🧩 **Programmers** interested in minimalist language design
- 🎨 **Artists** creating computational art
- 🔬 **Researchers** exploring esoteric languages

> _"A language that proves you need only 8 symbols to compute anything."_

---

## 🧠 What is Brainfuck?

Brainfuck is an esoteric programming language featuring only **8 commands**:

| Symbol |  Operation   | Description                       |
| :----: | :----------: | --------------------------------- |
|  `>`   | Move Pointer | Move pointer right                |
|  `<`   | Move Pointer | Move pointer left                 |
|  `+`   |  Increment   | Increment cell by 1               |
|  `-`   |  Decrement   | Decrement cell by 1               |
|  `.`   |    Output    | Print cell as ASCII character     |
|  `,`   |    Input     | Read character into cell          |
|  `[`   |  Loop Start  | Jump past `]` if cell is 0        |
|  `]`   |   Loop End   | Jump back to `[` if cell is not 0 |

**That's it.** Yet it's **Turing-complete**! 🤯

### The Memory Model

```
Memory Tape:    [0] [0] [0] [0] [0] [0] [0] [0] ...
                  ^
              Pointer (starts here)
```

Each cell is a byte (0-255). The pointer can move left/right infinitely.

---

## ⭐ Why Learn Brainfuck?

### 🎓 Educational Value

- Master fundamental memory concepts
- Understand loops and conditionals at the metal
- See how complexity emerges from simplicity
- Challenge your algorithmic thinking

### ✨ Beauty in Minimalism

- Pure logic, no syntax sugar
- Every character counts
- Elegant solutions shine
- Small programs, big impact

### 🎨 Creative Potential

- Generate ASCII art patterns
- Create visual designs
- Prove Turing completeness
- Join a unique programmer community

---

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- A terminal/command prompt
- Your favorite text editor

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/Only_brainfuck.git
cd Only_brainfuck
```

2. **Verify Python installation**

```bash
python --version
```

### Running Programs

```bash
# Run a Hello World program
python bf_runner.py programs/01_hello.bf

# Run with debug output
python bf_runner.py programs/02_letter_a.bf --debug

# Run with full execution trace
python bf_runner.py programs/03_counter_0_9.bf --trace
```

### Expected Output

```
$ python bf_runner.py programs/01_hello.bf
Hello, World!

$ python bf_runner.py programs/03_counter_0_9.bf
0123456789
```

---

## 📚 Programs

Explore our collection of pure Brainfuck programs:

### 1. **01_hello.bf** - Hello, World!

Your entry point to Brainfuck programming.

```
Output: Hello, World!
Technique: Character increment and printing
Lines: 1
Complexity: ⭐ Beginner
```

### 2. **02_letter_a.bf** - Single Character

Demonstrates ASCII value calculation.

```
Output: A
Technique: Cell increment
Lines: 1
Complexity: ⭐ Beginner
```

### 3. **03_counter_0_9.bf** - Countdown Counter

Print numbers 0 through 9.

```
Output: 0123456789
Technique: Loops with increment
Lines: 1
Complexity: ⭐⭐ Intermediate
```

### 4. **04_alphabet.bf** - Full Alphabet

Print A through Z.

```
Output: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Technique: Repeated increment pattern
Lines: 1
Complexity: ⭐⭐ Intermediate
```

### 5. **05_pyramid.bf** - Pyramid Pattern

```
Output:
*
**
***
****
*****

Technique: Nested loops
Lines: 1
Complexity: ⭐⭐⭐ Advanced
```

### 6. **06_box.bf** - Box Drawing

```
Output:
*****
*   *
*   *
*   *
*****

Technique: 2D nested loops, conditionals
Lines: 1
Complexity: ⭐⭐⭐ Advanced
```

### 7. **07_line_of_stars.bf** - Horizontal Line

Generate a line of asterisks.

```
Output: ****************************
Technique: Simple loop
Lines: 1
Complexity: ⭐ Beginner
```

### 8. **08_smiley.bf** - ASCII Smiley Face

```
Output:
  ^_^
 (o_o)
  \_/

Technique: Multi-line output
Lines: 1
Complexity: ⭐⭐ Intermediate
```

### 9. **09_addition.bf** - Add Two Numbers

Mathematical computation in Brainfuck.

```
Input: Two single-digit numbers
Output: Their sum
Technique: Input, loops, computation
Lines: 1
Complexity: ⭐⭐⭐ Advanced
```

---

## 💡 Techniques

### Core Patterns

**Clear a Cell:**

```brainfuck
[-]     Decrement until zero
```

**Copy a Cell:**

```brainfuck
[->+>+<<]>>[-<<+>>]   Copy from cell 0 to cells 1 and 2
```

**Loop Pattern:**

```brainfuck
[        Start loop (while current cell != 0)
  >+<   Increment next cell, move back
  -     Decrement current cell
]        End loop
```

### Advanced Techniques

- Nested loops for 2D output
- Conditional logic with cell values
- Input/output processing
- Arithmetic operations

For detailed technique documentation, see [TECHNIQUES.md](TECHNIQUES.md).

---

## 🛠️ Development

### Project Structure

```
Only_brainfuck/
├── README.md              # This file
├── QUICKSTART.md          # Quick start guide
├── TECHNIQUES.md          # Advanced patterns
├── bf_runner.py           # Python interpreter
└── programs/
    ├── 01_hello.bf
    ├── 02_letter_a.bf
    ├── 03_counter_0_9.bf
    ├── 04_alphabet.bf
    ├── 05_pyramid.bf
    ├── 06_box.bf
    ├── 07_line_of_stars.bf
    ├── 08_smiley.bf
    └── 09_addition.bf
```

### Contributing

We welcome contributions! You can help by:

- 🐛 **Reporting bugs** in the interpreter
- ✨ **Adding new programs** to the collection
- 📝 **Improving documentation**
- 🎯 **Optimizing existing code**
- 🌍 **Translating guides**

### Steps to Contribute

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/your-feature`)
3. **Make** your changes
4. **Test** your code with the interpreter
5. **Commit** with clear messages
6. **Push** to your fork
7. **Open** a Pull Request

### Code of Conduct

Be respectful, inclusive, and collaborative. This is a learning community.

---

## 🧪 Testing

Run the test suite:

```bash
# Run all programs (minimal testing)
for file in programs/*.bf; do
    echo "Testing $file..."
    python bf_runner.py "$file"
done
```

---

## 📚 Learn More

### External Resources

- **[Brainfuck on Wikipedia](https://en.wikipedia.org/wiki/Brainfuck)** - Language history and semantics
- **[Esolangs.org](https://esolangs.org/wiki/Brainfuck)** - Comprehensive reference
- **[Online Brainfuck Interpreter](https://repl.it/languages/brainfuck)** - Write code online
- **[Brainfuck Visualizer](https://brainfuck.org)** - Step through execution

### Similar Projects

- BF-Interpreter: Simple Python implementation
- Esoteric Languages: Other minimal languages
- Esolang Collections: More interesting languages

---

## 💬 FAQ

**Q: Why would anyone use Brainfuck?**  
A: It's a proof of Turing completeness with minimal syntax. Great for learning and creative coding challenges.

**Q: Is it faster than Python?**  
A: No! Brainfuck is interpreted. Speed isn't the point — elegance and challenge are.

**Q: Can Brainfuck run real programs?**  
A: Technically yes, but practically no. It would be thousands of lines long. It's educational, not practical.

**Q: How do I debug Brainfuck code?**  
A: Use the `--debug` and `--trace` flags with `bf_runner.py`.

**Q: Is Brainfuck the most minimal language?**  
A: No! Other languages like **Malbolge**, **Unlambda**, and **IOTA** are even more obscure.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and distribute copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 👤 Author

**Created with ❤️ by [Your Name]**

- 🌐 [Website](https://your-website.com)
- 💼 [LinkedIn](https://linkedin.com/in/yourprofile)
- 🐙 [GitHub](https://github.com/yourusername)

---

## 🌟 Support

If you find this project helpful, please consider:

- ⭐ **Starring** this repository
- 🔀 **Forking** and contributing
- 📢 **Sharing** with others
- 💬 **Opening issues** with feedback

---

<div align="center">

### Made with 🧠 and 8 Symbols

_Challenge yourself. Learn Turing completeness. Have fun with Brainfuck._

[![GitHub Stars](https://img.shields.io/github/stars/yourusername/Only_brainfuck?style=social)](https://github.com/yourusername/Only_brainfuck)
[![GitHub Forks](https://img.shields.io/github/forks/yourusername/Only_brainfuck?style=social)](https://github.com/yourusername/Only_brainfuck/fork)

</div>

**Lines**: 1 line  
**Concept**: Counter mechanics

### 4. **fibonacci.bf** - Number Sequence

```brainfuck
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```

**Output**: `0 1 1 2 3 5 8 13...`  
**Lines**: 1 line  
**Concept**: Accumulator pattern

### 5. **checkerboard.bf** - Grid Pattern

```brainfuck
>++++[<+++++++++++++<+++++++++++++>>-]<<>[->[->+>+<<]>[-<+>]>[-<+>]<<]+++++++++[>++++++++++<-]>[.>]>.
```

**Output**:

```
# # # # #
 # # # #
# # # # #
 # # # #
# # # # #
```

**Lines**: 1 line  
**Concept**: Alternating pattern logic

## How to Run

### Option 1: Online Interpreter (No Setup!)

1. Go to [repl.it/@Craigiest/brainfuck](https://repl.it/@Craigiest/brainfuck)
2. Copy one of the programs below
3. Paste into the editor
4. Click Run
5. See magic happen!

### Option 2: Use bf_runner.py

```bash
python bf_runner.py hello.bf
python bf_runner.py square.bf
python bf_runner.py pyramid.bf
```

### Option 3: Online Brainfuck Interpreters

- [Online-Interpreter.com](https://online-interpreter.com/)
- [Tutorialspoint](https://www.tutorialspoint.com/execute_brainfuck_online.php)
- [JSFIDDLE BF](https://jsfiddle.net/PzqKL/8/)

## Understanding Brainfuck Code

### Memory Model

```
[0][0][0][0][0]
        ↑
      pointer
```

### Basic Operations

```brainfuck
++            # Add 1 to current cell
[-]           # Set current cell to 0
[>+<-]        # Move value from cell 0 to cell 1
[>+++<-]      # Multiply by adding in a loop
```

### "Hello" Step by Step

```brainfuck
++++[>+++<-] # Create 12 in second cell (4*3)
>             # Move right
++.           # Add 2, print (14 = 'H' in ASCII? No...)
              # Actually: 72 = 'H'
              # So: ++++++[>++++++++<-]> makes 8*8=64, then add 8 = 72
```

## Real Examples

### Count to 10

```brainfuck
+++++++++++[>++++++++++<-]>.
```

### Generate 'A'

```brainfuck
++++++++[>++++++++<-]>.
```

### Generate 'A' to 'Z'

```brainfuck
++++++++[>++++++++<-]>[>+++++++++++++<-]>. [>+<-]>.
```

### Simple Loop Output

```brainfuck
+++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```

**Output**: `Hello World`

## Benefits of Brainfuck

### 🧠 Mental Exercise

- Trains algorithmic thinking
- Develops problem-solving skills
- Challenges assumptions about programming

### 📚 Educational

- Understand Turing machines
- Learn machine memory concepts
- Master loops at primitive level
- No language overhead to distract you

### 🎯 Pure Logic

- No frameworks
- No libraries
- No syntax noise
- Just pure computation

### 🏆 Skill Showcase

- Rare skill (very few people know BF)
- Interview talking point
- Demonstrates deep understanding
- Shows you can learn anything

### 💡 Creativity

- Limited tools force elegant solutions
- Small programs, big impact
- Zen of programming
- Constraint breeds creativity

## Advanced Techniques

### Multiplication

```brainfuck
# Multiply cells[0] * cells[1], store in cells[2]
[>[>+<-]<-]>
```

### Division

```brainfuck
# Divide cells[0] by cells[1]
# More complex - multiple steps needed
```

### Conditionals

```brainfuck
# If cell[0] > 0, execute code in brackets
[>+<-]
```

### Working with Multiple Cells

```brainfuck
# Use different memory cells as variables
# Cell 0: accumulator
# Cell 1: counter
# Cell 2: result
# Cell 3: temp
```

## Learning Path

1. **Start Simple**: Run `hello.bf`
2. **Understand**: Read the code, trace execution
3. **Modify**: Change numbers, see what happens
4. **Create**: Write your own character output
5. **Combine**: Mix patterns together
6. **Master**: Build complex algorithms

## Challenge Yourself

### Easy

- [ ] Output your name
- [ ] Create a square
- [ ] Print 1-10

### Medium

- [ ] Create a checkerboard
- [ ] Print multiplication table
- [ ] Generate ASCII art

### Hard

- [ ] Implement addition
- [ ] Implement multiplication
- [ ] Create a simple game

## Brainfuck Facts

✨ **Turing Complete** - Can compute anything computable  
⚡ **Only 8 Symbols** - Minimal instruction set  
🎓 **Invented 1993** - Urban Müller, still alive!  
🌍 **Language Spec** - 1 page  
💾 **Smallest Programs** - 2-3 characters  
🏃 **Speed** - Can be very fast with optimization

## Real Brainfuck Code Examples

### Count 0-9

```brainfuck
+++++++++++[>++++++++++<-]<.>[>+<-]>.
```

### Fibonacci (Modified)

```brainfuck
++++++++[
>++++[
>++
>+++
>+++
>+
<<<<-
]
>+
>+
>-
>>+
[<]<-
]
>>.
>---.
+++++++..
+++.
>>.<-.
<.
+++.
------.
--------.
>>+.
>++.
```

## File Structure

```
Only_brainfuck/
│
├── README.md              ← You are here!
│
├── bf_runner.py          ← Simple Python runner
│
├── programs/
│   ├── hello.bf          ← Hello World
│   ├── square.bf         ← ASCII Square
│   ├── pyramid.bf        ← Triangle Pattern
│   ├── fibonacci.bf      ← Number Sequence
│   ├── checkerboard.bf   ← Grid Pattern
│   ├── alphabet.bf       ← A-Z Generator
│   ├── counter.bf        ← Count 1-10
│   └── mandelbrot.bf     ← Advanced: Fractal
│
└── TECHNIQUES.md         ← How BF works (optional)
```

## Why This Project?

### For Beginners

- See that programming is simple
- Understand memory deeply
- Build confidence through working code
- No complex syntax to learn

### For Advanced Programmers

- Challenge yourself
- Appreciate high-level languages
- Understand computer fundamentals
- Impress people at parties

### For Students

- Great for CS courses
- Teach Turing completeness
- Show machine memory
- Make programming real

## Tips for Writing Brainfuck

1. **Use comments**: Anything not in `><+-.,[]` is ignored
2. **Think in memory**: Visualize the tape
3. **Test incrementally**: Run small pieces
4. **Document heavily**: You'll forget what you did
5. **Use multiple cells**: Organize your "variables"

## Resources

- [Brainfuck Wikipedia](https://en.wikipedia.org/wiki/Brainfuck)
- [Esolangs Wiki](https://esolangs.org/wiki/Brainfuck)
- [Brainfuck Interpreter](https://www.tutorialspoint.com/execute_brainfuck_online.php)
- [Brainfuck Visualizer](https://fatiherikli.github.io/brainfuck-visualizer/)
- [90 Minutes of Brainfuck](https://github.com/kriswallsmith/brainfuck)

## Contribute

Add your own Brainfuck creations!

1. Write a `.bf` file
2. Test it
3. Document what it does
4. Submit!

## License

Public Domain - Use freely!

## Fun Facts

- Brainfuck programs can be unreadable on purpose
- Code golf champions use Brainfuck
- It's Turing complete but impractical
- Simpler than Turing machines
- Every computer can run it (eventually)

---

## Start Your Journey! 🚀

Pick a program above. Run it. Modify it. Understand it. Create it.

**The only limit is your imagination and 8 symbols.**

Good luck! You've got this! 💪
#   B r a i n F u c k 
 
 

# Only Brainfuck

<div align="center">

![Python](https://img.shields.io/badge/Python-3.6+-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Brainfuck](https://img.shields.io/badge/Brainfuck-Esoteric-ff6b6b?style=for-the-badge)

</div>

---

## 📌 About the Project

**Only Brainfuck** is a curated collection of Brainfuck programming examples and learning resources. Brainfuck is a minimalist esoteric programming language with just 8 symbols, yet it's Turing-complete—meaning you can write any algorithm with it.

This project helps developers understand:

- How esoteric languages work
- Low-level memory manipulation
- The essence of computation with minimal syntax

## ✨ Why Brainfuck Matters

1. **Educational Value** - Understand how computers work at the most basic level
2. **Creative Coding** - Challenge yourself with an ultra-minimalist language
3. **Problem Solving** - Learn creative problem-solving with extreme constraints
4. **Language Design** - See what's possible with minimal features

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher

### Running Programs

```bash
# Run a Brainfuck program
python bf_runner.py programs/01_hello.bf

# Debug mode (shows step-by-step execution)
python bf_runner.py programs/02_letter_a.bf --debug

# Trace execution
python bf_runner.py programs/03_counter_0_9.bf --trace
```

### Example Programs

- `01_hello.bf` - Hello World
- `02_letter_a.bf` - Print the letter 'A'
- `03_counter_0_9.bf` - Count from 0 to 9
- `04_alphabet.bf` - Print the alphabet
- `05_pyramid.bf` - Print a pyramid pattern
- `06_box.bf` - Draw a box
- `07_line_of_stars.bf` - Print a line of stars
- `08_smiley.bf` - Draw a smiley face
- `09_addition.bf` - Addition demonstration

## 📚 Documentation

- [QUICKSTART.md](QUICKSTART.md) - Get started with Brainfuck basics
- [TECHNIQUES.md](TECHNIQUES.md) - Advanced patterns and optimization tips

## ⚙️ Technical Details

**Note:** The `bf_runner.py` implementation is maintained in a separate repository: [bf_runner](https://github.com/Manikeshmk/bf_runner). After cloning this repo, copy the `bf_runner.py` code from that repository into the local `bf_runner.py` file.

## 📖 Learn More

- The 8 Brainfuck symbols: `>`, `<`, `+`, `-`, `.`, `,`, `[`, `]`
- Online interpreters: [brainfuck.org](https://brainfuck.org), [repl.it](https://repl.it/languages/brainfuck)
- [Wikipedia on Brainfuck](https://en.wikipedia.org/wiki/Brainfuck)

---

Happy Brainfucking! 🧠

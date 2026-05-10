# Quick Start Guide

Welcome to Only_brainfuck! This guide will help you get started quickly.

## What is Brainfuck?

Brainfuck is a minimalist programming language with only **8 symbols**:

- `>` : Move pointer right
- `<` : Move pointer left
- `+` : Increment cell
- `-` : Decrement cell
- `.` : Output
- `,` : Input
- `[` : Start loop
- `]` : End loop

That's it! But with these 8 symbols, you can write ANY program (Turing complete).

## Getting Started

### Option 1: Use Python Runner

Requirements: Python 3.6+

**Run a program:**

```bash
cd Only_brainfuck
python bf_runner.py programs/01_hello.bf
```

**Debug a program:**

```bash
python bf_runner.py programs/02_letter_a.bf --debug
```

**Trace execution:**

```bash
python bf_runner.py programs/03_counter_0_9.bf --trace
```

### Option 2: Online Interpreters

No installation needed! Try these:

- [repl.it Brainfuck](https://repl.it/languages/brainfuck)
- [brainfuck.org](https://brainfuck.org)
- [Online Brainfuck Interpreter](https://www.tutorialspoint.com/execute_brainfuck_online.php)

Just copy-paste code from any `.bf` file and click run!

### Option 3: Other Interpreters

- **JavaScript**: [brainfuck-js](https://github.com/jsdf/brainfuck)
- **Node.js**: `npm install -g brainfuck`
- **Go**: [brainfuck-interpreter](https://github.com/brainfuck-implementations/go)

## Example Programs

### Simplest: Print 'A'

File: `programs/02_letter_a.bf`

```brainfuck
++++++++[>++++++++<-]>+.
```

What it does:

1. Create 8 in cell 0
2. Loop 8 times: add 8 to cell 1 (8×8=64)
3. Add 1 to get 65 (ASCII 'A')
4. Print it

Output: `A`

### Count 0-9

File: `programs/03_counter_0_9.bf`

Creates ASCII 48 ('0') then loops 10 times, incrementing and printing each digit.

Output: `0123456789`

### Print Alphabet

File: `programs/04_alphabet.bf`

Prints A through Z by creating 65 (ASCII 'A') and looping 26 times.

Output: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`

### Visual Patterns

File: `programs/05_pyramid.bf`

Creates visual patterns by printing characters in loops.

## Understanding the Programs

Let's trace through `02_letter_a.bf`:

```
++++++++  Cell 0 = 8
[         Loop (8 times)
  >       Move to cell 1
  +++++++ Add 8
  <       Back to cell 0
  -       Decrement
]         End loop
>         Move to cell 1 (now has 64)
+         Add 1 (now 65 = 'A')
.         Print
```

### Memory State During Execution

```
Step: ++++++++
Cell: [8][0]
      ^

Step: [>
Cell: [8][0]
         ^

Step: ++++++++<
Cell: [8][8]
      ^

Step: - (in loop, back to start)
Cell: [7][8]
      ^

... repeat 7 more times ...

Step: ] (loop ends when cell 0 = 0)
Cell: [0][64]
      ^

Step: >+.
Cell: [0][65]
         ^
Output: A
```

## Challenge: Write Your Own

### Challenge 1: Print 'Z'

Hint: ASCII value of 'Z' is 90

Solution: Find what multiplies to 90, or add to 65:

```brainfuck
++++++++[>++++++++++<-]>+.  (8*10+1=81... close!)
# Try: 9*10+1 = 91, then subtract 1
+++++++++[>++++++++++<-]>+-.
```

### Challenge 2: Print Two Characters

Print 'Hi':

- 'H' = 72
- 'i' = 105

Hint: Save 72, then modify to 105

### Challenge 3: Count Backwards from 5

Print: 54321

Hint: Start at ASCII '5' (53), then subtract to get '4', '3', etc.

## Tips & Tricks

1. **Clear a cell**: `[-]` decrements until zero
2. **Copy a value**: Use intermediate cells
3. **Count operations**: Group `+` symbols: `++++++` instead of + + + + + +
4. **Comment code**: Use anything that's not a BF symbol as a comment
5. **Test incrementally**: Build one piece at a time

## Common Issues

### "Nothing printed!"

- Check if output is a non-printable character (ASCII 0-31)
- Try adding 48 to get printable ASCII
- Use `--trace` to see what's happening

### "Program hangs!"

- You might have an infinite loop: `[+]`
- Check bracket matching
- Press Ctrl+C to stop

### "Wrong output!"

- Check ASCII values (A=65, a=97, 0=48, space=32)
- Trace through your logic step by step
- Use smaller test values first

## Learning Path

1. **Week 1**: Print characters (easiest, see concepts)
2. **Week 2**: Loops and counting (core skill)
3. **Week 3**: Arithmetic (addition, multiplication)
4. **Week 4**: Complex patterns (nested loops, memory management)
5. **Week 5+**: Real algorithms (sorting, fibonacci, mandelbot)

## Next Steps

1. Read [README.md](README.md) for philosophy and examples
2. Explore [TECHNIQUES.md](TECHNIQUES.md) for advanced patterns
3. Modify existing programs in `programs/` directory
4. Write your own program (start with printing your name)
5. Join the Brainfuck community!

## Resources

- **Tutorial**: See README.md "Understanding Brainfuck"
- **Specification**: [Brainfuck on Esolang](https://esolangs.org/wiki/Brainfuck)
- **Community**: [Brainfuck Subreddit](https://www.reddit.com/r/brainfuck)
- **Archive**: [Brainfuck Code Repository](https://www.iventech.com/brainfuck/)

## Have Fun!

Brainfuck is a celebration of computational simplicity. With just 8 symbols, you can:

- Generate beautiful patterns
- Solve mathematical problems
- Create interactive programs
- Expand your understanding of programming

The journey of writing Brainfuck teaches you that **elegance can be minimal** and **power can come from simplicity**.

Happy coding! 🎉

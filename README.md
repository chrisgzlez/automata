# Automata
This automaton reads its description from a plain text file passed as arguments in its execution creates an automaton able to interpret chains of characters from the CLI.

## Requirements
python > 3.10 or above

## Usage Guide
- exit -> exists the program
- reset -> resets the autamaton to its initial state and deletes its history
- chain -> you can pass any chain of caracter that you please, 
    the automaton will only process those that has as inputs

execution: 
```bash
python main.py file_with_automaton_definition
```
> **Note:** in case you your default python version isn't 3.x, command must be runned with `python3`

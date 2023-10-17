# Automata
## Requirements
python > 3.10 or above

## Usage Guide
exit -> exists the program
reset -> resets the autamaton to its initial state and deletes its history
chain -> you can pass any chain of caracter that you please, 
    the automaton will only process those that has as inputs

execution: 
```bash
python main.py file_with_automaton_definition
```
in case you are running ubuntu you must specify `python3` in the command

in case you don't have a python version bigger than 3.10 you may:
  - delete lines from 113 to 119 (match-case)
  - and indent the two lines to the level of the rest of the code


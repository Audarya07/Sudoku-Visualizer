# Sudoku Visualizer

```
![Sudoku Visualizer GIF](sudoku_gif.mp4)
```

Sudoku is a puzzle which can be quite complex to solve and that's why I have tried to solve it using a technique known as **Backtracking**.  

## How It Works
1. Backtracking tries to fill the cells one by one. 
2. Whenever we find that current digit cannot lead to a solution(shown by red cell), we remove it (backtrack) and try next digit.

I have implemented this simple Sudoku Visualizer in Python and made the GUI using **Pygame** - an awesome module provided by Python.

## Installation Guide
1. `git clone https://github.com/Audarya07/Sudoku-Visualizer.git`
2. Any Python 3 version
3. `pip install pygame`

## Contents of this Repository

* `sudoku.py` contains the code of which can be executed on command line by executing the command `python sudoku.py`
* `solver_gui.py` contains the GUI version of the sudoku visualizer (needs pygame installed) which can be executed on command line by executing the command `python solver_gui.py`
* `sudoku.png` - Please don't remove this image from the folder. This image works as icon of the application.
* `Sudoku.exe` - executable which can be directly run on Windows platform. 


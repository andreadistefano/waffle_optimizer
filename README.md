# Waffle Optimizer
Find solutions for [Waffle](https://wafflegame.net/). **This is not a solver**, as it requires the correct solution beforehand.

Most waffles get solved with optimal solutions (10 moves). Some waffles require 11 or 12.

No external dependencies. Tested on python 3.9

## Instructions
* Run `python main.py`
* Insert the number of the waffle you want to solve
* Press ENTER after each step

## To insert a new puzzle
* Fork the repository
* Inside the `waffles` folder, create a subfolder named with the number of the puzzle and pad it with zeros (ex: 27 -> 027)
* Inside the subfolder, create `start.txt` and `end.txt`, with the starting waffle and the solution. The format is
    ```
    X X X X X
    X _ X _ X
    X X X X X
    X _ X _ X
    X X X X X
    ```
* Open a PR
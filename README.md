# [🧮] Math Program (Problem 1)
## How to run
You can get the program here:
 <!-- INCEPE -->
[![Download Here](https://custom-icon-badges.demolab.com/badge/-Download-blue?style=for-the-badge&logo=download&logoColor=white "Download zip")](https://github.com/lates-codrin/math-program/archive/refs/tags/iteration-3.zip)
<!-- TERMINA -->

To run this program:
```bash
  python app.py
```


## [📜] Features

- Add numbers or insert at position in a list.
- Remove or replace numbers or sublists of a list.
- Get numbers with certain properties from list.
- Filter list to contain numbers with certain properties.
- Perform operations such as summation of elements, GCD(), MAX() on the list.
- Undo any operation made on the list.


## [🔨] Usage/Examples

### Add a number to the list
```bash
python app.py
```
Current list: my_list = []
```text
[1] Console-based
[2] Pygui-based
[3] Exit
Your choice: 1
```

```
add 10
```
Then the list would be: my_list = [10]

### Undo an operation
```bash
python app.py
```
Current list: my_list = []
```text
[1] Console-based
[2] Pygui-based
[3] Exit
Your choice: 1
```

```
add 100
```
Then the list would be: my_list = [100]
```
undo
```
Then the list would be: my_list = []


# [💾] Program Iterations (Versions)

## Iteration 1

- Created all of the features in 1 file.

## Iteration 2
- Started modularizing everything and adding checks (and asserts)
- Added console input, and validation of input.

## Iteration 3
- Improved console UI, and added expressions to complement numbers in the UI.
   - e.g Instead of inputting "2" and "replace 1 2" to replace 1 with 2 inside the list, simply type "replace 1 2".
- Added documentation (docstring) and how to use the program.

## Iteration 4
- Non-console UI launcher, using Dear PyGui

## Iteration 5
- Shortening of the run function inside the console ui launcher

## Iteration 6
- More validation of user input in #features, and updated pygui result text to display errors
## Lessons Learned

While building this project I learned that python allows me to do things that seemed impossible before. Before, code could take up from 10-20 lines, but now everything can basically be done in __one__ line, thanks to Python.

Thanks to this I could focus on coming up with better ideas; for example the undo() function. It seemed complicated at first, but after a bit of thinking I realised all I had to do is store previous version of the list inside a list array, something that would be very hard if not impossible to do with C++ (the language I used before).


## Authors

- [@lates-codrin](https://github.com/lates-codrin)


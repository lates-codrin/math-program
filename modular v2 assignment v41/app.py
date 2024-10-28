""" Task: Problem no. 1
    Author: Lates Codrin-Gabriel (codrin.lates@stud.ubbcluj.ro)
    Iteration: 5, 28.10.2024

    Version history will be made public after assignment goes past due.
    https://github.com/lates-codrin/math-program
"""
from ui.console import console_menu
from ui.pygui import gui_menu

choice = int(input("[1] Console-based\n[2] Pygui-based\n[3] Exit\nYour choice: "))
if choice == 1: console_menu()
elif choice== 2: gui_menu()
#gui_menu()
#console_menu()



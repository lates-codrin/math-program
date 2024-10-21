""" Task: Problem no. 1
    Author: Lates Codrin-Gabriel (codrin.lates@stud.ubbcluj.ro)
    Iteration: 4, 21.10.2024
"""
from ui.console import console_run
from ui.pygui import gui_run

choice = int(input("[1] Console-based\n[2] Pygui-based\n[3] Exit\nYour choice: "))
{1: console_run, 2: gui_run}.get(choice, lambda: None)()


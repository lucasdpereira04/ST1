'''
*******************************
Author:
u3257896 Assessment 2 Problem 5 29/09/2024
Programming:Object Oriented Inventory Management System
*******************************
'''

from Controller import BoatController
from View import create_gui

if __name__ == "__main__":
    print("Starting application...")
    controller = BoatController()
    create_gui(controller)
    print("Application running...")


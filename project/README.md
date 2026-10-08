🧮 Python Calculator
🎥 Video Demo: <PASTE YOUR YOUTUBE VIDEO URL HERE>
👨‍💻 Author:

[YOUR NAME]

📚 Course:

CS50's Introduction to Programming with Python (CS50P)

📌 Description

🧮 Python Calculator is my final project for Harvard University's CS50's Introduction to Programming with Python (CS50P). It is a simple, interactive command-line calculator written entirely in Python.

The main purpose of this project is to create a useful calculator while demonstrating the Python programming concepts learned throughout the course. The calculator allows users to perform basic mathematical calculations directly from the terminal.

The program supports four basic arithmetic operations:

➕ Addition
➖ Subtraction
✖️ Multiplication
➗ Division

The user enters two numbers and selects an operator. The program performs the requested calculation and displays the result.

✨ Features

The calculator includes several useful features:

➕ Basic Calculations

Users can perform addition, subtraction, multiplication, and division.

For example:

Enter first number: 20
Enter operator (+, -, *, /): +
Enter second number: 10
Result: 30

🔄 Multiple Calculations

The program runs inside a loop, which means users can perform multiple calculations without restarting the program.

This makes the calculator more convenient and interactive.

🚪 Easy Exit

Users can enter:

q


at any input stage to exit the calculator.

The program then displays:

Goodbye!

🛡️ Error Handling

The program handles incorrect input instead of crashing.

For example, if the user enters text instead of a number, the program displays an appropriate error message.

It also checks whether the entered mathematical operator is valid.

🚫 Division by Zero Protection

The calculator prevents division by zero.

For example:

Enter first number: 10
Enter operator (+, -, *, /): /
Enter second number: 0
Error: Cannot divide by zero.


This prevents the program from terminating unexpectedly.

🧩 Project Structure

The project contains four
The calculator supports four basic arithmetic operations: addition, subtraction, and multiplication, and division. The user enters two numbers and selects an operator. The program then performs the requested calculation and displays the result. The calculator continues running so that the user can perform multiple calculations during the same program session. The user can enter q when prompted for a number or operator to quit the program.

The main program is contained in project.py. This file contains the main function, which handles the user interface and controls the calculator program. It also contains separate functions for addition, subtraction, multiplication, and division. There is also a calculate function that determines which mathematical operation should be performed based on the operator entered by the user. Keeping the mathematical operations in separate functions makes the program easier to understand, test, and maintain.

The program also includes error handling. If the user enters something that is not a valid number, the program displays an error message instead of crashing. The program also checks for invalid operators. Division by zero is handled separately because Python cannot perform a normal division by zero. In that situation, the program displays an appropriate error message and allows the user to continue using the calculator.

The file test_project.py contains tests written using pytest. These tests verify that the calculator's individual functions work correctly. The tests check addition, subtraction, multiplication, division, division by zero, valid operators, and invalid operators. Testing the functions separately helped ensure that the calculator produces the expected results for different inputs.

The file requirements.txt contains the project's external dependency, pytest. The calculator itself only uses Python's built-in features, so no additional libraries are required to run the main program. Pytest is included because it is needed to execute the automated tests required for the project.

One design choice I made was to keep the calculator command-line based rather than creating a graphical interface. A command-line application is simpler to implement and allows the project to focus on Python programming concepts such as functions, loops, conditional statements, exception handling, user input, and testing. I also chose to create individual functions for each mathematical operation rather than putting all of the calculations directly inside main. This makes the code more organized and makes each operation easier to test.

Another design choice was to use a loop so that users can perform multiple calculations without restarting the program. The program also allows the user to quit easily by entering q. Overall, this project demonstrates the use of Python functions, loops, conditionals, exception handling, user input, modules, and automated testing.

This calculator is intentionally simple, but it demonstrates the core programming concepts learned during CS50P and provides a useful foundation that could be expanded in the future with features such as powers, square roots, percentages, calculation history, or a graphical user interface.
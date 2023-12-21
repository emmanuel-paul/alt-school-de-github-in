#Alt school first semester DE Exam hands on project

Hi, welcome to my first semester Data Engineering hands on project at Altschool.
The goal of this assignment is to assess my understanding on object-oriented programming
(OOP) concepts in Python. I was tasked with implementing two classes, Expense and
ExpenseDatabase, to model and manage financial expenses.

Classes Overview:
Expense Class:
Attributes:
1. id: A unique identifier generated as a UUID string.
2. title: A string representing the title of the expense.
3. amount: A float representing the amount of the expense.
4. created_at: A timestamp indicating when the expense was created (UTC).
5. updated_at: A timestamp indicating the last time the expense was updated (UTC).
Methods:
1. __init__: Initializes the attributes.
2. update: Allows updating the title and/or amount, updating the updated_at timestamp.
3. to_dict: Returns a dictionary representation of the expense.
ExpenseDB class
Manages a collection of Expense objects.
Attributes:
1. expenses: A list storing Expense instances.
Methods:
1. __init__: Initializes the list.
2. add_expense: Adds an expense.
3. remove_expense: Removes an expense.
4. get_expense_by_id: Retrieves an expense by ID.
5. get_expense_by_title: Retrieves expenses by title.
6. to_dict: Returns a list of dictionaries representing expenses.

 HOW TO CLONE THIS PROJECt?
    To clone this project, 
    use (git clone) command on your terminal
    git clone https://github.com/emmanuel-paul/alt-school-de-github-in


HOW TO RUN THE CODE?
 firstly, you clone the repository from github to local machine(terminal).
 install python on your computer.
 run the script using 'python main.py' or 'python3 main.py' depending on your python version.
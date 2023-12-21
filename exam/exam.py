"""
Expense Class:
Represents an individual financial expense.
Attributes:
1. id: A unique identifier generated as a UUID string.
2. title: A string representing the title of the expense.
3. amount: A float representing the amount of the expense.
4. created_at: A timestamp indicating when the expense was created (UTC).
5. updated_at: A timestamp indicating the last time the expense was updated (UTC)

"""

import uuid
from datetime import datetime, timezone

"""
__init__ :this method initializes the attributes.
datetime.utcnow(): an update method that allows updating the title and/or amount of the
expense.
a to_dict method that returns a dictionary representation of the expense.
__init__ method to initialize the expenses list.
"""
class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.updated_at



        
     def update(self, title=None, amount=None):
        if title != None:
            self.title = title
        if amount != None:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []

    def add_expense(self, title, amount):
        expense = Expense(title, amount)
        self.expenses.append(expense)

    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
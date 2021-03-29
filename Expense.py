class Expense(object):
    def __init__(self, id, date, amount, num_affected, paid):
        self.id = None
        self.date = None
        self.amount = None
        self.num_affected = None
        self.paid = None
        self.cards_attached = 0

    @classmethod
    def new_expense(cls):
        return cls()

    @classmethod
    def add_expense(cls, line):
        new = Expense.new_expense()
        new.type = line[0]
        new.date = line[1]
        new.amount = line[2]
        new.num_affected = line[3]
        new.paid = line[4]
        new.id = new.type + new.date[new.date.find('/'):]
        return new
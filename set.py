class Set:
    def __init__(self, name, era, year, number):
        self.name = name
        self.era = era
        self.year = year
        self.total_number = number
        self.cards = [] # use chaining for cards with same num
class Era:
    def __init__(self, name, start_year, end_year, number):
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.total_number = number
        self.sets = [] # use chaining for sets with same year
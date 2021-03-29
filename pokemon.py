class Pokemon:
    def __init__(self, name, number, generation):
        self.name = name
        self.number = number
        self.generation = generation
 
    def get_name(self):
        return self.name
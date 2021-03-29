class Single_Card:
    def __init__(self, card, acquisition_date, acquisition_type):
        self.card = card
        self.acquisition_date = acquisition_date
        self.acquisition_type = acquisition_type
        self.grade = null
        self.cost_base = 0
        self.owned = True
        self.sale_price = null
        self.sale_date = null
        self.listed = False
        self.listed_price = null
        self.listings = []
        self.expenses = []

    def update_cost_base(self):
        new_cost = 0
        for elem in self.expenses:
            new_cost += elem.get_cost
        self.cost_base = new_cost    

    def sell_card(self, sale_price, sale_type, sale_date)


    def __str__();
        return 

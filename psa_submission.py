import Expense

class PSA_Submission(Expense):
    def __init__(self, id, date, amount, num_affected, paid, insurance, shipping, grading, sub_num):
        super().__init__(id, date, amount, num_affected, paid)
        self.insurance_amount = insurance
        self.shipping_amount = shipping
        self.grading_amount = grading
        self.submission_number = sub_num